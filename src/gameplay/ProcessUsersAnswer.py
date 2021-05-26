if __name__ != "__main__":
    from config.rich_configuration import console
    from operator import itemgetter
    from src.emphasize import emphasize, confirmation

    class ProcessUsersAnswer:
        def __init__(self, answer, correct, answers_summary, question):
            self.correct = correct
            self.answer = answer
            self.answers_summary = answers_summary
            self.answer_is_correct = correct == answer
            self.question = question

        def create_blank_space_at_ending(self, r=3):
            for i in range(r):
                print()

        def redemption(self):
            if self.correct == input("Powtorz wyraz: "):
                confirmation("Dobrze!")
            else:
                console.print("[red]Zle![/]")

        def display_false(self):
            self.answers_summary["invalid"].append(self.question)
            correct, answer = itemgetter("correct", "answer")(vars(self))
            console.print("Chujnia", style="red")
            explanation = ""
            for index, char in enumerate(correct):
                if index < len(answer) and correct[index] == answer[index]:
                    explanation += char
                else:
                    explanation += emphasize(char)
            console.print(answer)
            console.print(explanation)

            self.redemption()

        def display_true(self):
            self.answers_summary["valid"].append(self.question)
            console.print("Okej", style="green")

        def main(self):
            self.display_true() if self.answer_is_correct else self.display_false()
            self.create_blank_space_at_ending()