# 🎓 University of Hertfordshire - SQL Database Project

This repository contains the **SQL Assignment** project for the **Data Mining and Discovery** module, developed by **Cristina Baron Suarez**. The project focuses on creating a comprehensive and realistic university database using **SQLite** and **Python** for data simulation.

## 📚 Project Overview
The goal of this project is to:
- Generate synthetic data representing the University of Hertfordshire's structure: faculties, departments, degrees, modules, professors, students, and enrollments.
- Use **Python (Pandas & NumPy)** for data creation (`dbCSV.py`).
- Use **SQLite** to create tables, define constraints, and populate them using CSV files (`SQLite_script.sql`).

## 🔍 Key Features
✅ **Realistic Data Generation:**  
- 1000 students with names, genders, nationalities, and randomized degree assignments.
- Faculties, degrees, modules, professors, and departments reflecting university structure.
- Data privacy: partial postcodes and anonymized phone numbers.

✅ **Python Automation:**  
- Run `dbCSV.py` to generate CSVs for all tables in the `data/` directory.

✅ **Database Creation with SQL:**  
- Use `SQLite_script.sql` to:
  - Create tables with appropriate constraints and relationships (primary keys, foreign keys, unique constraints).
  - Import CSV data into the database.
  - Enforce referential integrity.

## ⚙️ How to Use
### 1️⃣ Generate Data
Ensure you have Python installed with `pandas` and `numpy`.
```bash
python dbCSV.py

