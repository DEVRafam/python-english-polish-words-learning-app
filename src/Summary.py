if __name__ != "__main__":
    from operator import itemgetter
    from src.emphasize import emphasize
    from config.rich_configuration import console

    def compute_accuraty(invalid, valid):
        try:
            return round(len(valid) * 100 / (len(invalid) + len(valid)), 2)
        except ZeroDivisionError:
            return 0

    class DisplaySummary:
        def __init__(self, answers_summary):
            invalid, valid = itemgetter("invalid", "valid")(answers_summary)

            self.answers_summary = answers_summary
            self.invalid = invalid
            self.valid = valid
            self.accuraty = compute_accuraty(invalid=invalid, valid=valid)

        def display_accuraty(self):
            data = emphasize(self.accuraty)
            console.print(f"Answer's accuraty: {data}%")

        def display_valid_answers(self):
            data = emphasize(len(self.valid))
            console.print(f"- Correct answers: [green]{data}[/]")

        def display_invalid_answers(self):
            data = emphasize(len(self.invalid))
            console.print(f"- Invalid answers: [red]{data}[/]")

        def main(self):
            print()
            self.display_accuraty()
            self.display_valid_answers()
            self.display_invalid_answers()
            print()
