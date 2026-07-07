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
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Email")
    print("5. Delete Student")
    print("6. Add Course")
    print("7. Enroll Student in Course")
    print("8. Add Assessment")
    print("9. Record Grade")
    print("10. View Student Report")
    print("11. Dashboard")
    print("12. Student Ranking")
    print("13. Mark Attendance")
    print("14. View Attendance")
    print("15. Add Teacher Comment")
    print("0. Exit")


    choice = input("Choose an option: ")

    if choice == "1":

        student_id = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")

        student = Student(student_id, name, email)
        gradebook.add_student(student)

    elif choice == "2":

        gradebook.view_students()

    elif choice == "3":

        keyword = input("Enter Student ID or Name: ")

        student = gradebook.search_student(keyword)

        if student:
            student.display_info()
        else:
            print("Student not found.")

    elif choice == "4":

        student_id = input("Student ID: ")
        email = input("New Email: ")

        gradebook.update_student(student_id, email)

    elif choice == "5":

        student_id = input("Student ID: ")
        gradebook.delete_student(student_id)

    elif choice == "6":

        code = input("Course Code: ")
        name = input("Course Name: ")

        course = Course(code, name)

        gradebook.add_course(course)

    elif choice == "7":

        student_id = input("Student ID: ")
        course_code = input("Course Code: ")

        gradebook.enroll_student(student_id, course_code,)

    elif choice == "8":

        course_code = input("Course Code: ")

        print("1. Quiz")
        print("2. Exam")
        print("3. Project")

        assessment_type = input("Choose type: ")

        title = input("Title: ")
        max_score = float(input("Max Score: "))

        if assessment_type == "1":
            assessment = Quiz(title, max_score)

        elif assessment_type == "2":
            assessment = Exam(title, max_score)

        elif assessment_type == "3":
            assessment = Project(title, max_score)

        else:
            print("Invalid choice.")
            continue

        gradebook.add_assessment(course_code, assessment)

    elif choice == "9":

        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        title = input("Assessment Title: ")
        score = float(input("Score: "))

        gradebook.record_grade(
            student_id,
            course_code,
            title,
            score
        )

    elif choice == "10":
        student_id = input("Student ID: ")
        gradebook.show_report(student_id)

    elif choice == "11":
        gradebook.dashboard()

    elif choice == "12":
        gradebook.ranking()

    elif choice == "13":

        student_id = input("Student ID: ")

        print("1. Present")
        print("2. Absent")
        print("3. Late")

        choice = input("Choose status: ")

        if choice == "1":
            status = "Present"
        elif choice == "2":
            status = "Absent"
        elif choice == "3":
            status = "Late"
        else:
            print("Invalid choice.")
            continue

        gradebook.mark_attendance(student_id, status)
       
    elif choice == "14":

        gradebook.show_attendance()

    elif choice == "15":

        student_id = input("Student ID: ")
        comment = input("Teacher Comment: ")

        gradebook.add_comment(student_id, comment)

    elif choice == "0":

        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
