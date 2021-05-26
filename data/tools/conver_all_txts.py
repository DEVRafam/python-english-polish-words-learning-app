if __name__ != "__main__":
    from os import listdir
    from pathlib import Path
    import io
    import json

    from data.tools.convert_txt_into_json import Converter
    from src.emphasize import confirmation, emphasize

    class ConvertAll:
        def __init__(self, root, merged_output_name=False):
            self.root = root
            self.merged_output_name = merged_output_name
            self.merged_words = []
            self.main()

        @property
        def txt_dir_path(self):
            return Path.joinpath(self.root, "data", "txt")

        def merge_words(self, new_words):
            # avoid having duplicated dictionaries
            [self.merged_words.append(item) for item in new_words if item not in self.merged_words]

        def export_merged_words(self):
            p = Path.joinpath(self.root, "data", self.merged_output_name)
            with io.open(p, mode="w+") as f:
                json.dump(self.merged_words, f)
                print("\n----------------------")
                confirmation(
                    f"All json files have been merged successfully into {emphasize(self.merged_output_name)}!"
                )

        def main(self):
            for txt_file in listdir(self.txt_dir_path):
                file_name = txt_file.split(".")[0]
                txt_to_json_converter = Converter(
                    root=self.root,
                    txt_file_path=Path.joinpath(self.txt_dir_path, txt_file),
                    json_file_name=file_name,  #
                )
                if self.merged_output_name:
                    self.merge_words(new_words=txt_to_json_converter.words)
            if self.merged_output_name:
                self.export_merged_words()
