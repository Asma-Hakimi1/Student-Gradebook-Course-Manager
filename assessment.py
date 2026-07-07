class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score / self.max_score) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 80:
            return "Excellent"
        elif percentage >= 60:
            return "Good"
        elif percentage >= 50:
            return "Passed"
        else:
            return "Failed"

    def display_info(self):
        print(f"{self.title} - Max Score: {self.max_score}")
