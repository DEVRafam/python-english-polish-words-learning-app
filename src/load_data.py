import json
from pathlib import Path

data_path = Path.joinpath(Path(__file__).parent.absolute(), "..", "data", "main.json")
words = None

with open(data_path, "r") as f:
    words = json.load(f)
