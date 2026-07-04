from assessment import Assessment


class Quiz(Assessment):

    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def display_info(self):
        print(f"Quiz: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 80:
            return "Great quiz result!"
        elif percentage >= 50:
            return "Good job."
        else:
            return "Needs more practice."
