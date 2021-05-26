from operator import itemgetter


if __name__ != "__main__":
    from src.draw_new_verb import draw_new_verb
    from src.gameplay.Gameplay import Gameplay
    from src.Summary import DisplaySummary
    from src.logging.SaveResultLog import SaveResultLog
    from src.logging.analyzation.AnalyzeProgress import AnalyzeProgress
    from time import time

    class App:
        def __init__(self, words, root_path, analysis_parameters):
            # from params
            self.words = words
            self.root_path = root_path
            self.analysis_parameters = analysis_parameters
            # computed
            self.already_drawn_words = []
            self.total_draws_count = 0
            self.answers_summary = {"valid": [], "invalid": []}
            self.data_for_logs = {
                "deleted_words": [],
                "words_made_strong": [],
                "words_made_weak": [],
                "words_removed_from_strong": [],
                "words_removed_from_weak": [],
            }
            self.start_time = time()

        def make_new_draw(self):
            return draw_new_verb(words_list=self.words, already_drawn_words=self.already_drawn_words)

        def make_analysis(self):
            return AnalyzeProgress(
                answers_summary=self.answers_summary,
                root_path=self.root_path,
                analysis_parameters=self.analysis_parameters,
                data_for_logs=self.data_for_logs,  #
            ).main()

        def end_gameplay(self):
            end_time = time()
            answers_summary, root_path = itemgetter("answers_summary", "root_path")(vars(self))

            DisplaySummary(answers_summary).main()
            points = self.make_analysis()
            SaveResultLog(
                answers_summary=answers_summary,
                root_path=root_path,
                points=points,
                numbers_of_draws=self.total_draws_count,
                duration=end_time - self.start_time,
                data_for_logs=self.data_for_logs,  #
            ).main()

        def create_gameplay(self):
            try:
                while len(self.words) != len(self.already_drawn_words):
                    self.total_draws_count += 1
                    Gameplay(self).main(draw=self.make_new_draw())
                else:
                    self.end_gameplay()
            except KeyboardInterrupt:
                self.end_gameplay()