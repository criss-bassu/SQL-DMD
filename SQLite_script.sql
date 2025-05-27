CREATE TABLE University (
     universityID   INTEGER PRIMARY KEY,
     universityName TEXT NOT NULL,
	 country        TEXT, 
     county         TEXT, 
     city           TEXT, 
     postcode       TEXT, 
     foundationYear INTEGER , 
     universityAge  INTEGER
);

CREATE TABLE Faculty (
     facultyID               INTEGER PRIMARY KEY,
     facultyName             TEXT NOT NULL,
     universityID            INTEGER NOT NULL,
     FOREIGN KEY (universityID) REFERENCES University(universityID)
);

CREATE TABLE Degree (
     degreeID          INTEGER PRIMARY KEY, 
     degreeName        TEXT NOT NULL,
     facultyID         INTEGER NOT NULL,
     category          TEXT,
     FOREIGN KEY (facultyID) REFERENCES Faculty(facultyID)
);

CREATE TABLE Department (
     departmentID      INTEGER PRIMARY KEY,
     departmentName    TEXT NOT NULL,
     facultyID         INTEGER NOT NULL,
     FOREIGN KEY (facultyID) REFERENCES Faculty(facultyID)
);

CREATE TABLE Professor ( 
     professorID             INTEGER  NOT NULL PRIMARY KEY, 
     email                   TEXT  NOT NULL UNIQUE, 
     name                    TEXT  NOT NULL, 
     surname                 TEXT  NOT NULL, 
     phone                   TEXT, 
     departmentID            INTEGER  NOT NULL, 
     universityID            INTEGER  NOT NULL,
	 FOREIGN KEY (departmentID) REFERENCES Department(departmentID),
	 FOREIGN KEY (universityID) REFERENCES University(universityID)
);

CREATE TABLE Student (
     studentID               INTEGER  NOT NULL PRIMARY KEY, 
     email                   TEXT  NOT NULL UNIQUE, 
     name                    TEXT  NOT NULL, 
     surname                 TEXT  NOT NULL, 
     gender                  TEXT, 
     nationality             TEXT, 
     startDate               DATE, 
     finishDate              DATE, 
     degreeID                INTEGER  NOT NULL, 
     universityID            INTEGER  NOT NULL,
	 FOREIGN KEY (degreeID) REFERENCES Degree(degreeID),
	 FOREIGN KEY (universityID) REFERENCES University(universityID) 
);

CREATE TABLE Module (
     moduleID                INTEGER PRIMARY KEY,
     moduleName              TEXT NOT NULL,
     credits                 INTEGER,
	 degreeID                INTEGER  NOT NULL, 
     professorID             INTEGER  NOT NULL,
     departmentID            INTEGER NOT NULL,
	 FOREIGN KEY (degreeID) REFERENCES Degree(degreeID)
	 FOREIGN KEY (professorID) REFERENCES Professor(professorID)
     FOREIGN KEY (departmentID) REFERENCES Department(departmentID)
);

CREATE TABLE Enrollment (
    term              TEXT,
    year              TEXT,
    grade             REAL,
    studentID         INTEGER NOT NULL,
    moduleID          INTEGER NOT NULL,
    PRIMARY KEY (studentID, moduleID),
    FOREIGN KEY (studentID) REFERENCES Student(studentID),
    FOREIGN KEY (moduleID) REFERENCES Module(moduleID)
);

-- foreign kys available
PRAGMA foreign_keys = ON;


-- INSERTING INTO TABLES
INSERT INTO University (universityID, universityName, country, county, city, postcode, foundationYear, universityAge)
SELECT universityID, universityName, country, county, city, postcode, foundationYear, universityAge
FROM university_csv;

INSERT INTO Faculty (facultyID, facultyName, universityID)
SELECT facultyID, facultyName, universityID
FROM faculty_csv;

INSERT INTO Degree (degreeID, degreeName, facultyID, category)
SELECT degreeID, degreeName, facultyID, category
FROM degree_csv;

INSERT INTO Department (departmentID, departmentName, facultyID)
SELECT departmentID, departmentName, facultyID
FROM department_csv;

INSERT INTO Professor (professorID, email, name, surname, phone, departmentID, universityID)
SELECT professorID, email, name, surname, phone, departmentID, universityID
FROM professor_csv;

INSERT INTO Student (studentID, email, name, surname, gender, nationality, startDate, finishDate, degreeID, universityID)
SELECT studentID, email, name, surname, gender, nationality, startDate, finishDate, degreeID, universityID
FROM student_csv;

INSERT INTO Module (moduleID, moduleName, credits, degreeID, professorID, departmentID)
SELECT moduleID, moduleName, credits, degreeID, professorID, departmentID
FROM module_csv;

INSERT INTO Enrollment (term, year, grade, studentID, moduleID)
SELECT term, year, grade, studentID, moduleID
FROM enrollment_csv;


-- DROP CSVs
DROP TABLE degree_csv;
DROP TABLE department_csv;
DROP TABLE enrollment_csv;
DROP TABLE faculty_csv;
DROP TABLE module_csv;
DROP TABLE professor_csv;
DROP TABLE student_csv;
DROP TABLE university_csv;

-- DROP tables
-- DROP TABLE enrollment;
-- DROP TABLE module;
-- DROP TABLE professor;
-- DROP TABLE student;
-- DROP TABLE department;
-- DROP TABLE degree;
-- DROP TABLE faculty;
-- DROP TABLE university;