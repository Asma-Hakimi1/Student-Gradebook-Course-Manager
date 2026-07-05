class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.assessments = []

def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)
            print("Student enrolled successfully.")
        else:
            print("Student is already enrolled.")

def add_assessment(self, assessment):
        self.assessments.append(assessment)
        print("Assessment added successfully.")

def find_assessment(self, title):
        for assessment in self.assessments:
            if assessment.title == title:
                return assessment
        return None

def display_info(self):
        print("\n===== Course Information =====")
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Enrolled Students:", len(self.students))

        if self.assessments:
            print("Assessments:")
            for assessment in self.assessments:
                assessment.display_info()
        else:
            print("No assessments added.")
