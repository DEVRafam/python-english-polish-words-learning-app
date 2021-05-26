if __name__ != "__main__":
    from operator import itemgetter
    from config.rich_configuration import console
    from src.emphasize import emphasize

    class DisplayIntroMessage:
        def __init__(self, polish, english):
            self.polish = polish
            self.english = english

        def is_phraze(self):
            return len(self.english.split(" ")) > 1

        def english_message(self):
            english = itemgetter("english")(vars(self))
            length = emphasize(len(english))
            first_letter = emphasize(english[0])
            english_message = f"- The word starts with letter {first_letter}\n- {length} characters long"

            if self.is_phraze():
                words_count = emphasize(len(english.split(" ")))
                english_message = f"- The phraze starts with letter {first_letter}\n- {length} characters long\n- {words_count} words long"

            return english_message

        def polish_message(self):
            polish = itemgetter("polish")(vars(self))
            return f"Word in polish: {emphasize(polish)}"

        def main(self):
            console.print(emphasize("-------------"))
            console.print(self.polish_message())
            console.print(self.english_message())
            console.print(emphasize("-------------"))
