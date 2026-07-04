from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from project import Project


class Gradebook:

    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

# ---------------- Students ----------------

    def add_student(self, student):
        self.students[student.get_id()] = student
        print("Student added successfully.")

    def search_student(self, keyword):
        for student in self.students.values():
            if student.get_id() == keyword or student.get_name().lower() == keyword.lower():
                return student
        return None


    def update_student(self, student_id, new_email):
        if student_id in self.students:
            self.students[student_id].set_email(new_email)
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id in self.students:

            for course in self.courses.values():
                if student_id in course.students:
                    course.students.remove(student_id)

            del self.students[student_id]

            if student_id in self.grades:
                del self.grades[student_id]

            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return

        for student in self.students.values():
            student.display_info()
            print()
