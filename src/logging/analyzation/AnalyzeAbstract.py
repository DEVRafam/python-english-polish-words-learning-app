if __name__ != "__main__":
    from abc import ABC, abstractmethod
    from pathlib import Path
    import json

    class AnalyzeAbstract(ABC):
        # REQUIRED PROPERTIES
        @property
        @abstractmethod
        def root_path(self):
            ...

        @property
        @abstractmethod
        def answers_summary(self):
            pass

        @property
        @abstractmethod
        def analysis_parameters(self):
            pass

        # METHODS

        def uniques_english_words(self, data):
            uniques = set([])
            if type(data) == dict:
                for log in data + [self.answers_summary]:
                    for word in log["valid"] + log["invalid"]:
                        uniques.add(word["english"])
            elif type(data) == list:
                for item in data:
                    uniques.add(item["english"])

            return uniques

        def read_json_file(self, filename, dir="results"):
            p = Path.joinpath(self.root_path, "logs", dir, filename)
            with open(p, "r") as result:
                return json.load(result)
