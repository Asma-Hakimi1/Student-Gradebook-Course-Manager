from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook

gradebook = Gradebook()

while True:

    print("\n===== Student Gradebook Manager =====")
    print("1. Add Student")


    choice = input("Choose an option: ")

    if choice == "1":

        student_id = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")

        student = Student(student_id, name, email)
        gradebook.add_student(student)
