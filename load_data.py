
import json

FILE_PATH = "users.json"

def load_data():
    with open(FILE_PATH, "r") as handle:
        return json.load(handle)