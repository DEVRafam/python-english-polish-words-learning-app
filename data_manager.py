from pathlib import Path
from data.tools.conver_all_txts import ConvertAll

root = Path(__file__).parent.absolute()

ConvertAll(root, merged_output_name="main.json")