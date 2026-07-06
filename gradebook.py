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

# ---------------- Courses ----------------

    def add_course(self, course):
        self.courses[course.course_code] = course
        print("Course added successfully.")

    def enroll_student(self, student_id, course_code,):

        if student_id not in self.students:
            print("Student not found.")
            return

        if course_code not in self.courses:
            print("Course not found.")
            return

        self.students[student_id].enroll_course(course_code)
        self.courses[course_code].add_student(student_id)

        print("Enrollment completed.")

# ---------------- Assessments ----------------

    def add_assessment(self, course_code, assessment):

        if course_code not in self.courses:
            print("Course not found.")
            return

        self.courses[course_code].add_assessment(assessment)

# ---------------- Grades ----------------

    def record_grade(self, student_id, course_code, assessment_title, score):

        if student_id not in self.students:
            print("Student not found.")
            return

        if course_code not in self.courses:
            print("Course not found.")
            return

        assessment = self.courses[course_code].find_assessment(assessment_title)

        if assessment is None:
            print("Assessment not found.")
            return

        if score < 0 or score > assessment.max_score:
            print("Invalid score.")
            return

        if student_id not in self.grades:
            self.grades[student_id] = {}

        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}

        self.grades[student_id][course_code][assessment_title] = score

        print("Grade recorded successfully.")

# ---------------- Average ----------------

    def calculate_average(self, student_id, course_code):

        if student_id not in self.grades:
            return 0

        if course_code not in self.grades[student_id]:
            return 0

        total = 0
        count = 0

        course = self.courses[course_code]

        for assessment in course.assessments:

            if assessment.title in self.grades[student_id][course_code]:

                score = self.grades[student_id][course_code][assessment.title]

                total += assessment.calculate_percentage(score)
                count += 1

        if count == 0:
            return 0

        return total / count

# ---------------- Result ----------------

    def get_result(self, average):
        if average >= self.passing_grade:
            return "Passed"
        else:
            return "Failed"

    def get_letter_grade(self, average):

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

# ---------------- Report ----------------

    def show_report(self, student_id):

        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        print("\n===== Student Report =====")
        print("ID:", student.get_id())
        print("Name:", student.get_name())
        print("Email:", student.get_email())

        for course_code in student.courses:

            print("\nCourse:", course_code)
                  
            if student_id in self.grades and course_code in self.grades[student_id]:

                for title, score in self.grades[student_id][course_code].items():
                    print(title, ":", score)

                average = self.calculate_average(student_id, course_code)

                print("Average:", round(average, 2))
                print("Letter Grade:", self.get_letter_grade(average))
                print("Result:", self.get_result(average))

            if student_id in self.comments:
                print("Teacher Comment:", self.comments[student_id])
