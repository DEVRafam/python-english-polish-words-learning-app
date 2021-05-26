if __name__ != "__main__":
    from pathlib import Path
    from datetime import datetime
    from time import ctime
    import json

    from src.emphasize import confirmation

    class SaveResultLog:
        def __init__(self, answers_summary, root_path, points, duration, numbers_of_draws, data_for_logs):
            self.answers_summary = answers_summary
            self.root_path = root_path
            self.points = points
            self.duration = duration
            self.numbers_of_draws = numbers_of_draws
            self.data_for_logs = data_for_logs

            self._log_name = None

        def generate_log_file_name(self):
            self._log_name = datetime.now().strftime("%d-%m-%Y_%H.%M.%S") + ".json"
            return self._log_name

        def create_path(self):
            return Path.joinpath(self.root_path, "logs", "results", self.generate_log_file_name())

        def main(self):
            with open(self.create_path(), "w+") as write_file:
                json.dump(
                    {
                        "date": ctime(),
                        "session_duration[s]": round(self.duration),
                        "numbers_of_draws": self.numbers_of_draws,
                        "accuracy[%]": self.data_for_logs["accuraty"],
                        "invalid": self.answers_summary["invalid"],
                        "valid": self.answers_summary["valid"],
                        "points_generated_during_session": self.points,
                        "progress": self.data_for_logs,
                    },
                    write_file,
                )

            print()
            confirmation(f'LOG with name "{self._log_name}" has been created succesfully!')
