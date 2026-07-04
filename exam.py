from assessment import Assessment


class Exam(Assessment):

    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def display_info(self):
        print(f"Exam: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 55:
            return "Passed exam."
        else:
            return "Failed exam."
