import io


if __name__ != "__main__":
    import json
    from pathlib import Path

    from config.rich_configuration import console  # 4 dev purposes only 🚀
    from src.emphasize import confirmation
    from src.logging.analyzation.AnalyzeAbstract import AnalyzeAbstract

    class CrucialWordsSaver(AnalyzeAbstract):
        def __init__(self, answers_summary, root_path, analysis_parameters, data_for_logs, words):
            self._root_path = root_path
            self._answers_summary = answers_summary
            self._analysis_parameters = analysis_parameters
            self._data_for_logs = data_for_logs
            self._words = words

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

        @property
        def words(self):
            return self._words

        def translate_wordstype(self, wordstype):
            """Translate one of ('strong','weak','archived') to either list or string that associate with App.data_for_logs key"""
            return {
                "weak": {
                    "add": "words_made_weak",
                    "remove": "words_removed_from_weak",  #
                },
                "strong": {
                    "add": "words_made_strong",
                    "remove": "words_removed_from_strong",  #
                },
                "archived": "deleted_words",  #
            }[wordstype]

        def convert_words(self, words_list, present_data_unique_english=[]):
            """Convert  list of only english words to list that matches schema:\n{english:str, polish:str}"""
            return [
                item
                for item in self.analysis_parameters["API"]["data_copy"]
                if item["english"] in words_list and item["english"] not in present_data_unique_english
            ]

        def find_differences(self, words_list, present_data_unique_english, wordstype):
            translated_keys = self.translate_wordstype(wordstype)
            # either strong or weak
            if type(translated_keys) == dict:
                new_words = [item for item in words_list if item not in present_data_unique_english]
                missing_words = [item for item in present_data_unique_english if item not in words_list]

                self.data_for_logs[translated_keys["add"]] = self.convert_words(new_words)
                self.data_for_logs[translated_keys["remove"]] = self.convert_words(missing_words)
            # archive case only
            else:
                new_words = [item for item in words_list if item not in present_data_unique_english]
                new_words = self.convert_words(new_words)
                self.data_for_logs[translated_keys] = new_words
                # handle archivization
                archived_p = self.analysis_parameters["API"]["path"]
                data = self.analysis_parameters["API"]["data_copy"]
                [data.remove(item) for item in new_words if item in data]
                with io.open(archived_p, mode="w+") as f:
                    json.dump(data, f)
                # remove item from strong.json
                strong_words = self.read_json_file("strong.json", dir="progress")
                [strong_words.remove(item) for item in new_words if item in strong_words]
                strong_p = Path.joinpath(self.root_path, "logs", "progress", "strong.json")
                with open(strong_p, "w+") as f:
                    json.dump(strong_words, f)

        def save_words(self, words_list, wordstype):
            p = Path.joinpath(self.root_path, "logs", "progress", f"{wordstype}.json")
            #
            present_data = self.read_json_file(filename=f"{wordstype}.json", dir="progress")
            present_data_unique_english = list(self.uniques_english_words(present_data))
            # basically check whether at least one new strong|weak word has occurred
            if present_data_unique_english != words_list:
                converted_words = self.convert_words(words_list, present_data_unique_english)
                self.find_differences(words_list, present_data_unique_english, wordstype)
                with open(p, "w+") as file_writer:
                    json.dump(converted_words + present_data, file_writer)

                confirmation(f"{wordstype} words has been exported successfully!")

        def main(self):
            self.save_words(self.words["strong_words"], "strong")
            self.save_words(self.words["weak_words"], "weak")
            self.save_words(self.words["words_to_delete"], "archived")