if __name__ != "__main__":

    class CrucialWordsDefiner:
        def __init__(self, points, analysis_parameters):
            self._points = points
            self._analysis_parameters = analysis_parameters

        @property
        def points(self):
            return self._points

        @property
        def analysis_parameters(self):
            return self._analysis_parameters

        def delete_word_condition(self, value):
            return value >= self.analysis_parameters["points"]["define_mastered"]

        def weak_word_condition(self, value):
            return value <= self.analysis_parameters["points"]["define_weak"]

        def strong_word_condition(self, value):
            return value >= self.analysis_parameters["points"]["define_strong"]

        def main(self):
            weak_words = []
            strong_words = []
            words_to_delete = []

            for key, value in self.points.items():
                if self.delete_word_condition(value):
                    words_to_delete.append(key)
                    continue
                elif self.weak_word_condition(value):
                    weak_words.append(key)
                    continue
                elif self.strong_word_condition(value):
                    strong_words.append(key)

            return {
                "weak_words": weak_words,
                "strong_words": strong_words,
                "words_to_delete": words_to_delete,  #
            }
