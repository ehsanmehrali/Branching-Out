
import json

FILE_PATH = "load_data.py"

def load_data():
    with open(FILE_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)