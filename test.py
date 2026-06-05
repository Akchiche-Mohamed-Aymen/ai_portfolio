from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

data_path = BASE_DIR  / "data.json"
print(data_path)