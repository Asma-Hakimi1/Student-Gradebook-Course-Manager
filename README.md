# Student Gradebook & Course Manager

## Student Name
Asma Hakimi

## Project Title
Student Gradebook & Course Manager

## Project Description
This is a terminal-based Python application that helps manage students, courses, assessments, and grades. The program allows users to add students, create courses, enroll students, add assessments, record grades, calculate averages, and generate student reports.

## Features
- Add, view, search, update, and delete students.
- Add courses.
- Enroll students in courses.
- Add quizzes, exams, and projects.
- Record student grades.
- Calculate average grades.
- Display pass/fail results.
- Display letter grades (A, B, C, D, F).
- Dashboard showing total students, courses, and assessments.
- Student ranking based on average grades.

## Project Files
- main.py
- student.py
- course.py
- assessment.py
- quiz.py
- exam.py
- project.py
- gradebook.py

## OOP Concepts Used

### Encapsulation
The Student class uses private attributes such as:
- __student_id
- __name
- __email

These attributes are accessed using getter and setter methods.

### Inheritance
The following classes inherit from the Assessment class:
- Quiz
- Exam
- Project

### Method Overriding
The Quiz, Exam, and Project classes override:
- display_info()
- grade_message()

## Data Structures
The project uses:
- Lists to store courses, students, and assessments.
- Dictionaries to store students, courses, and grades.

## Custom Features
1. Letter Grade (A, B, C, D, F)
2. Dashboard
3. Student Ranking

## How to Run

1. Open the project folder.
2. Make sure all Python files are in the same folder.
3. Run:

'''bash
python main.py
'''
4. Use the menu to manage students, courses, assessments, and grades.

## Main Workflow

1. Add a student.
2. Add a course.
3. Enroll the student in the course.
4. Add an assessment.
5. Record the student's grade.
6. View the student report.

## Author

Asma Hakimi
