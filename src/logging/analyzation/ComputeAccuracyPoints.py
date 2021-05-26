if __name__ != "__main__":
    from pathlib import Path
    from os import listdir
    from collections import defaultdict

    from src.logging.analyzation.AnalyzeAbstract import AnalyzeAbstract

    class ComputeAccuracyPoints(AnalyzeAbstract):
        def __init__(self, answers_summary, root_path, analysis_parameters):
            self._answers_summary = answers_summary
            self._root_path = root_path
            self._analysis_parameters = analysis_parameters

        @property
        def root_path(self):
            return self._root_path

        @property
        def analysis_parameters(self):
            return self._analysis_parameters

        @property
        def answers_summary(self):
            return self._answers_summary

        # METHODS

        def get_latest_results(self):
            p = Path.joinpath(self.root_path, "logs", "results")
            logs_files_names = listdir(p)
            return [self.read_json_file(filename=log) for log in logs_files_names]

        def main(self):
            points = defaultdict(int)
            for log in self.get_latest_results() + [self.answers_summary]:
                for word in log["invalid"]:
                    points[word["english"]] -= self.analysis_parameters["points"]["decrease_rate"]
                for word in log["valid"]:
                    points[word["english"]] += self.analysis_parameters["points"]["increase_rate"]

            return dict(points)
