import random

class Question:
    def __init__(self, text, choices):
        self.text = text
        self.choices = choices
        self.answer = None

    def ask(self):
        print(self.text)
        for idx, choice in enumerate(self.choices):
            print(f"{idx + 1}. {choice}")
        while True:
            try:
                choice = int(input("Choose an option (1/2/3/4): ")) - 1
                if 0 <= choice < len(self.choices):
                    self.answer = choice
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

class Survey:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def conduct(self):
        for question in self.questions:
            question.ask()

    def show_results(self):
        print("\nSurvey Results:")
        for idx, question in enumerate(self.questions):
            print(f"Q{idx + 1}: {question.text}")
            print(f"Your Answer: {question.choices[question.answer]}")

class SurveyGame:
    def __init__(self):
        self.survey = Survey()
        self.create_survey()

    def create_survey(self):
        questions = [
            Question("What is your favorite color?", ["Red", "Blue", "Green", "Yellow"]),
            Question("What is your favorite animal?", ["Dog", "Cat", "Elephant", "Tiger"]),
            Question("What is your favorite food?", ["Pizza", "Burger", "Pasta", "Sushi"]),
            Question("What is your favorite hobby?", ["Reading", "Sports", "Music", "Traveling"])
        ]
        for question in questions:
            self.survey.add_question(question)

    def play(self):
        print("Welcome to the Survey Game!")
        self.survey.conduct()
        self.survey.show_results()

if __name__ == "__main__":
    game = SurveyGame()
    game.play()
