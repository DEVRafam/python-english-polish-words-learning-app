if __name__ != "__main__":
    import io
    from pathlib import Path
    import json
    from datetime import datetime
    from src.emphasize import confirmation, emphasize
    import random
    import string

    class Converter:
        def __init__(self, txt_file_path, root, json_file_name=None):
            self._txt_file_path = txt_file_path
            self._root = root
            self._json_file_name = self.json_file_name_validator(json_file_name)
            self.words = self.load_txt_data()

            self.save_as_json()

        @property
        def root(self):
            return self._root

        @property
        def txt_file_path(self):
            return self._txt_file_path

        @property
        def json_file_name(self):
            return self._json_file_name

        def json_file_id(self, val):
            print(val)
            file_name = val.split(".")[0]
            json_id = "_" + "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            return file_name + json_id + ".json"

        def json_file_name_validator(self, val):
            if type(val) == str:
                if val[-5:] == ".json":
                    return val
                return val + ".json"
            # generate unique json file name
            return self.json_file_id(datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".json")

        def gen_json_dir_path(self):
            return Path.joinpath(self.root, "data", "json", self.json_file_name)

        def load_txt_data(self):
            data = io.open(self.txt_file_path, mode="r", encoding="utf-8").read()
            words = []
            for verb in data.split("\n"):
                splited_verb = verb.split("- ")
                if len(splited_verb) == 2:
                    english = splited_verb[0].lower()
                    polish = splited_verb[1].lower()
                    words.append({"english": english, "polish": polish})

            return words

        def save_as_json(self):
            with open(self.gen_json_dir_path(), "w+") as f:
                json.dump(self.words, f)
                confirmation(emphasize(self.json_file_name) + " has been created successfully")
