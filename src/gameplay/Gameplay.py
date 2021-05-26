if __name__ != "__main__":
    from operator import itemgetter
    from config.rich_configuration import console
    from src.gameplay.DisplayIntroMessage import DisplayIntroMessage
    from src.gameplay.ProcessUsersAnswer import ProcessUsersAnswer

    class Gameplay:
        def __init__(self, app):
            vars(self).update(vars(app))
            self.draw = None

        def display_draw_number(self):
            number = self.total_draws_count
            console.print(f"Draw number: [magenta]{number}[/]")

        def handle_intro_message(self):
            self.display_draw_number()
            english, polish = itemgetter("english", "polish")(self.draw)
            #
            DisplayIntroMessage(english=english, polish=polish).main()

        def get_users_answer(self):
            return input("My answer: ")

        def process_users_answer(self):
            answer = self.get_users_answer()
            correct = self.draw["english"]
            #
            return ProcessUsersAnswer(
                answer=answer, correct=correct, answers_summary=self.answers_summary, question=self.draw
            ).main()

        def main(self, draw):
            self.draw = draw
            self.handle_intro_message()
            return self.process_users_answer()
