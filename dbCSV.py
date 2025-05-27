import numpy as np
import pandas as pd
import random

# Number of samples
n = 1000

## 'University' table
university_id = [1]
university_name = ['University of Hertfordshire']
country = ['England']
county = ['Hertfordshire']
city = ['Hatfield']
postcode = ['AL10'] # less specific for data privacy reasons
foundation_year = [1952]
universityAge = pd.Timestamp.now().year - 1952  # Interval Data

# Create the university dataframe
university = pd.DataFrame({
    'universityID': university_id,
    'universityName': university_name,
    'country': country,
    'county': county,
    'city': city,
    'postcode': postcode,
    'foundationYear': foundation_year,
    'universityAge': universityAge
})

## 'Student' table
# Generate a list of numbers from 1 to n in order
student_id = np.arange(1, n + 1)

# Randomly generate gender 'Male' or 'Female'
gender = np.random.choice(['Male', 'Female'], n)  # Nominal data

# Depending on the gender, the student will have either a female or a male name
first_name = []
for i in range(n):
    if gender[i] == 'Male':
        first_name.append(np.random.choice([
            'Carlos', 'Pedro', 'Alvaro', 'Jose', 'Jairo', 'Mateo', 'Antonio', 'Ivan',
            'Oscar', 'Ruben', 'Elmar', 'David', 'Rodrigo', 'Jose', 'Miguel', 'Ignacio',
            'Danila', 'Luca', 'Helmut', 'Guillermo', 'William', 'Elio', 'Luis', 'Rafael',
            'Javier', 'Eduardo', 'Juan', 'James', 'Hugo', 'Charles', 'Peter', 'Hariz',
            'Pir', 'Nouman', 'Ghamees', 'Michael', 'Nick', 'Louis', 'Raphael', 'Joan',
            'Eric', 'Adrian', 'Sergio', 'Thomas'
        ], 1)[0])
    else:
        first_name.append(np.random.choice([
            'Pia', 'Marta', 'Marina', 'Cristina', 'Ana', 'Maria', 'Lucia', 'Paula',
            'Esther', 'Luisa', 'Elena', 'Julia', 'Martha', 'Taylor', 'Christine', 'Lucy',
            'Paola', 'Khadija', 'Sana', 'Kinza', 'Rena', 'Carmen', 'Mar', 'Samantha',
            'Selena', 'Sabrina', 'Tate', 'Madison', 'Marie', 'Ariana', 'Ava', 'Bebe',
            'Camila', 'Hailee', 'Kate', 'Olivia'
        ], 1)[0])

# Randomly generate last name
surname = np.random.choice([
    'Garcia', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Perez', 'Sanchez',
    'Bonvie', 'Benito', 'Rojano', 'Suarez', 'Baron', 'Prieto', 'Peralta', 'Escribano',
    'Campos', 'Carrobles', 'Gomez', 'Castro', 'Ruiz', 'Cordon', 'Bautista', 'Ortiz',
    'Arco', 'Montoro', 'Ramirez', 'Salas', 'Paakkinen', 'Hutter', 'Costa', 'Rubiales',
    'Delgado', 'Zaragoza', 'Correal', 'Caro', 'Roy'
], n)

# Randomly generate nationality
nationality = np.random.choice([
    'USA', 'China', 'India', 'Pakistan', 'Spain', 'Portugal', 'Germany', 'England',
    'Nigeria', 'Ireland', 'Wales', 'Scotland', 'Norway', 'Finland', 'Russia', 'Mexico',
    'Peru', 'France', 'Argentina', 'Australia'
], n)

# 20% of the students will have NULL in the attibute 'gender' and 'nationality'
maskGender = np.random.rand(n) < 0.2
maskNationality = np.random.rand(n) < 0.2
gender[maskGender] = ''
nationality[maskNationality] = ''

# Generate student email based on the studentID
email = []
for i in range(n):
    email.append(str(student_id[i]) + '@gmail.com')

# Generate start and finish date of the student's degree
start_date = []
finish_date = []
for i in range(n):
    # Randomly generate start date (YYYY-MM-DD)
    year = str(np.random.randint(1960, 2024))
    month = str(np.random.randint(1, 13)).zfill(2)
    day = str(np.random.randint(1, 29)).zfill(2)
    start_date.append(pd.to_datetime(f"{year}-{month}-{day}"))
    # if start_date was more than 4 years ago, add 3 years to the start date
    if start_date[i] < pd.to_datetime('2020-09-01'):
        finish_date.append(start_date[i] + pd.DateOffset(years = 3))
    else:
        finish_date.append(None)

# Randomly generate degree names
degrees = ['Computer Science', 'Data Science', 'Artificial Intelligence', 'Engineering',
    'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Medicine', 'Economics', 'Business',
    'Law', 'Psychology', 'Accounting and Finance', 'Marketing', 'History', 'Geography',
    'Philosophy', 'Sociology', 'Criminology', 'Education', 'Politics']

# Assigns an ID to each degree
degree_dict = {degree: i + 1 for i, degree in enumerate(degrees)}

# Assign each student to a random degree
dic_student_degree = {student: np.random.choice(list(degree_dict.keys())) for student in student_id}

# Create the student dataframe
student = pd.DataFrame({
    'studentID': student_id,
    'email': email,
    'name': first_name,
    'surname': surname,
    'gender': gender,
    'nationality': nationality,
    'startDate': start_date,
    'finishDate': finish_date,
    'degreeID': [degree_dict[degree] for degree in dic_student_degree.values()],
    'universityID': university_id * n
})

## 'Faculty' table
faculties = {
    1: 'Faculty of Computer Science and Engineering',
    2: 'Faculty of Natural Sciences',
    3: 'Faculty of Medicine and Health Sciences',
    4: 'Faculty of Economics and Business',
    5: 'Faculty of Law and Social Sciences',
    6: 'Faculty of Humanities'
}

# Assign a faculty to each degree
faculty_degrees = {
    1: [1, 2, 3, 4],            # Faculty of Computer Science and Engineering
    2: [5, 6, 7, 8],            # Faculty of Natural Sciences
    3: [9],                     # Faculty of Medicine and Health Sciences
    4: [10, 11, 13, 14],        # Faculty of Economics and Business
    5: [12, 15, 19, 20, 21],    # Faculty of Law and Social Sciences
    6: [16, 17, 18, 22]         # Faculty of Humanities
}

# Create the faculty dataframe
faculty = pd.DataFrame({
    'facultyID': list(faculties.keys()),
    'facultyName': list(faculties.values()),
    'universityID': university_id * len(faculties)
})

## 'Degree' table
# Decide, for each student, if they're doing undergraduate or postgraduate.
dic_degree_category = {student: np.random.choice(['Undergraduate', 'Postgraduate']) for student in student_id}

# Get the facultyID for each degree that is taught
faculty_ids = []
for degree_id in degree_dict.values():
    for faculty_id, grados in faculty_degrees.items():
        if degree_id in grados:
            faculty_ids.append(faculty_id)
            break

# Create the degree dataframe
grado = pd.DataFrame({
    'degreeID': list(degree_dict.values()),
    'degreeName': list(degree_dict.keys()),
    'facultyID': faculty_ids[:len(degree_dict)],
    # Decide whether a certain degree belongs to an undergraduate or postgraduate program
    'category': [np.random.choice(['Undergraduate', 'Postgraduate']) for _ in degree_dict]
})

## 'Module' table
# List of template string for module names
module_templates = ["Introduction to {degree}",
                    "{degree} Fundamentals",
                    "Advanced Topics in {degree}",
                    "{degree} Project",
                    "Research Methods in {degree}",
                    "Ethics and Professional Practice in {degree}"]

module_dict = {}
module_id = 1
# Iterate through each degree
for degree in degrees:
    # Iterate through the list of module templates
    for template in module_templates:
        module_name = template.format(degree = degree) # Replace '{degree}' for the actual degree name
        module_dict[module_id] = module_name # Assign an ID to the module name
        module_id += 1

# Assign each degreeID its corresponding moduleIDs
degree_module = {}
module_id = 1
# Iterate through the degreeIDs
for deg_id in range(1, len(degrees) + 1):
    modules_for_degree = [] # Saves the moduleIDs for the current degree
    # Iterate through the number of modules
    for _ in range(len(module_templates)):
        modules_for_degree.append(module_id) # Assigns the moduleID to the current degree
        module_id += 1
    # Associate the current degreeID with its corresponding moduleIDs
    degree_module[deg_id] = modules_for_degree

## 'Professor' table
professor_name = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Elijah', 'Sophia', 'James', 'Amelia', 'Benjamin',
    'Mia', 'Charlotte', 'Henry', 'Isabella', 'Ethan', 'Harper', 'Alexander', 'Evelyn', 'Sebastian', 'Gabriel']

professor_surname = ['Williams', 'Taylor', 'Anderson', 'Clark', 'Harris', 'Baker', 'Mitchell', 'Carter', 'Evans',
    'Parker', 'Scott', 'Reed', 'Morris', 'Ward', 'Watson', 'Brooks', 'Murphy', 'Bell', 'Cole', 'Bennett']

# The professor's email will be their name + surname + '@gmail.com'
professor_email = []
for i in range(len(professor_name)):
    professor_email.append(str(professor_name[i]).lower() + str(professor_surname[i]).lower() + '@gmail.com')

# Generate IDs for the professors
professor_id = np.arange(1, len(professor_name) + 1)

# Generate UK number phones
professor_phone = []
for i in range(len(professor_id)):
    if random.random() < 0.3:  # 30% chances of the phone number being null
        professor_phone.append(None)
    else:
        professor_phone.append('+44 7********' + str(random.randint(00, 99)))

## 'Department' table
departments = ['Computing and Software Engineering', 'Data and AI', 'Mechanical and Electrical Engineering',
    'Mathematics and Statistics', 'Natural Sciences', 'Health and Medicine', 'Economics and Finance',
    'Business and Marketing', 'Law and Criminology', 'Social and Behavioral Sciences',
    'Humanities and Philosophy', 'Politics and International Studies']

# Assign an ID to each department
department_dict = {department: i + 1 for i, department in enumerate(departments)}

# Assign the modules to the corresponding departments
dict_department_modules = {
    1: [1, 2, 3, 4, 5, 6],
    2: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    3: [19, 20, 21, 22, 23, 24],
    4: [25, 26, 27, 28, 29, 30],
    5: [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
    6: [49, 50, 51, 52, 53, 54],
    7: [55, 56, 57, 58, 59, 60, 79, 80, 81, 82, 83, 84],
    8: [61, 62, 63, 64, 65, 66, 85, 86, 87, 88, 89, 90],
    9: [67, 68, 69, 70, 71, 72, 115, 116, 117, 118, 119, 120],
    10: [73, 74, 75, 76, 77, 78, 109, 110, 111, 112, 113, 114],
    11: [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108],
    12: [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]
}

# Randomly assign each professor to a unique department
dept_ids = list(range(1, len(departments) + 1))
prof_ids = list(range(1, len(professor_id) + 1))
random.shuffle(prof_ids)

dic_professor_department = {}
for i in range(len(dept_ids)):
    dic_professor_department[prof_ids[i]] = dept_ids[i]
for i in range(len(dept_ids), len(prof_ids)):
    dic_professor_department[prof_ids[i]] = random.choice(dept_ids)

# Assign modules to professors(same department)
dic_module_professor = {}
for mod_id in range(1, 133):
    department_id = next(dept for dept, mods in dict_department_modules.items() if mod_id in mods)
    # List of professors that belong to the same department
    eligible_professors = [p_id for p_id, dept_id in dic_professor_department.items() if dept_id == department_id]
    # Randomly assign one of the professors to the module
    dic_module_professor[mod_id] = random.choice(eligible_professors)

## 'Module' table
degree_ids = []
department_ids = []
for mod_id in module_dict.keys():
    # Find the degree and department for each module
    deg_id = next((d_id for d_id, mods in degree_module.items() if mod_id in mods), None)
    dep_id = next((dpt_id for dpt_id, mods in dict_department_modules.items() if mod_id in mods), None)
    degree_ids.append(deg_id)
    department_ids.append(dep_id)

professor_ids = [dic_module_professor.get(m_id, None) for m_id in module_dict]

# Generate the 'module' dataframe
module = pd.DataFrame({
    'moduleID': list(module_dict.keys()),
    'moduleName': list(module_dict.values()),
    'credits': np.random.randint(6, 12, len(module_dict)),
    'degreeID': degree_ids,
    'professorID': pd.array(professor_ids, dtype = pd.Int64Dtype()),
    'departmentID': department_ids
})

# Generate the 'Professor' dataframe
professor = pd.DataFrame({
    'professorID': professor_id,
    'email': professor_email,
    'name': professor_name,
    'surname': professor_surname,
    'phone': professor_phone,
    'departmentID': [dic_professor_department[p] for p in professor_id],
    'universityID': university_id * len(professor_id)
})

# Assign the departments to each faculty
faculty_department = {
    1: [1, 2, 3],          # Faculty of Computer Science and Engineering
    2: [4, 5],             # Faculty of Natural Sciences
    3: [6],                # Faculty of Medicine and Health Sciences
    4: [7, 8],             # Faculty of Economics and Business
    5: [9, 10],            # Faculty of Law and Social Sciences
    6: [11, 12]            # Faculty of Humanities
}

# Create the 'Department' dataframe
department = pd.DataFrame({
    'departmentID': list(department_dict.values()),
    'departmentName': list(department_dict.keys()),
    # Get the facultyID by iterating over each departmentID (values of department_dict)
    'facultyID': [next((fid for fid, depts in faculty_department.items() if dept_id in depts), None) for dept_id in department_dict.values()]
})

## 'Enrollment' table
enrollment = pd.DataFrame(columns = ['term', 'year', 'grade', 'studentID', 'moduleID'])
enrollment_rows = []

# Iterate over each row in the 'student' DataFrame
for _, row in student.iterrows():
    st_id = row['studentID'] # Get the studentID from the current row
    deg_cat = dic_degree_category.get(st_id, 'Undergraduate').lower() # Get the degree category of the student ('Undergraduate' if the ID is not found)
    fdate = row['finishDate'] # Get the finish date of the student
    module_ids = module['moduleID'].tolist() # Get a list of moduleIDs

    # If the student has completed their studies
    if pd.notnull(fdate):
        # Undergraduate students
        if deg_cat == 'undergraduate':
            # Assign module marks for the first two years (12 modules, 6 per year, 3 per term).
            for i, m_id in enumerate(module_ids[:12]):
                year = 1 if i < 6 else 2   # Ordinal Data
                term = 1 if i % 6 < 3 else 2
                grade = np.random.uniform(50, 100) # Randomly assign a grade in between 50 and 100.
                enrollment_rows.append({
                    'term': term, 'year': year, 'grade': round(grade, 2),
                    'studentID': st_id, 'moduleID': m_id
                })
        # Postgraduate students
        elif deg_cat == 'postgraduate':
            # Assign module marks for one year (12 modules, 6 per term).
            for i, m_id in enumerate(module_ids[:12]):
                year = 1
                term = 1 if i < 6 else 2
                grade = np.random.uniform(50, 100)
                enrollment_rows.append({
                    'term': term, 'year': year, 'grade': round(grade, 2),
                    'studentID': st_id, 'moduleID': m_id
                })

enrollment = pd.DataFrame(enrollment_rows)

# Merge to get the startDate of each student
enrollment = enrollment.merge(
    student[['studentID','startDate']], 
    on = 'studentID', 
    how = 'left')

# Calculate the year in which they are studying this 'year'
enrollment['enrollmentYear'] = enrollment['startDate'].dt.year + (enrollment['year'] - 1)

# Defining the cutoff year
current_year = pd.Timestamp.now().year

# The enrollmentYear cannot be greater than the current year
enrollment.loc[enrollment['enrollmentYear'] > current_year, 'grade'] = None

# Remove auxiliar columns
enrollment.drop(columns = ['startDate', 'enrollmentYear'], inplace = True)

# Save the dataframes to CSV files
university.to_csv('data/university_csv.csv', index = False)
student.to_csv('data/student_csv.csv', index = False)
faculty.to_csv('data/faculty_csv.csv', index = False)
grado.to_csv('data/degree_csv.csv', index = False)
module.to_csv('data/module_csv.csv', index = False)
professor.to_csv('data/professor_csv.csv', index = False)
department.to_csv('data/department_csv.csv', index = False)
enrollment.to_csv('data/enrollment_csv.csv', index = False)