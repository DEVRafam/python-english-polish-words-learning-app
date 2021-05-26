if __name__ != "__main__":
    from config.rich_configuration import console  # 4 dev purposes only 🚀
    from src.logging.analyzation.ComputeAccuracyPoints import ComputeAccuracyPoints
    from src.logging.analyzation.crucial_words.Definer import CrucialWordsDefiner
    from src.logging.analyzation.crucial_words.Saver import CrucialWordsSaver

    class AnalyzeProgress:
        def __init__(self, answers_summary, root_path, analysis_parameters, data_for_logs):
            self._root_path = root_path
            self._answers_summary = answers_summary
            self._analysis_parameters = analysis_parameters
            self._data_for_logs = data_for_logs

        @property
        def answers_summary(self):
            return self._answers_summary

        @property
        def root_path(self):
            return self._root_path

        @property
        def analysis_parameters(self):
            return self._analysis_parameters

        @property
        def data_for_logs(self):
            return self._data_for_logs

        def make_crucial_words_definer(self, points):
            return CrucialWordsDefiner(
                points=points,
                analysis_parameters=self.analysis_parameters,  #
            ).main()

        def make_crucial_words_saver(self, words):
            return CrucialWordsSaver(
                answers_summary=self.answers_summary,
                root_path=self.root_path,
                analysis_parameters=self.analysis_parameters,
                data_for_logs=self.data_for_logs,
                words=words,
            ).main()

        def main(self):
            points = ComputeAccuracyPoints(self.answers_summary, self.root_path, self.analysis_parameters).main()
            words = self.make_crucial_words_definer(points)
            self.make_crucial_words_saver(words)

            return points
