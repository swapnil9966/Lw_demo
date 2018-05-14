import json
import os

def load_config_file():
    try:
        JSON_FILE_PATH = os.path.normpath(os.path.abspath(os.pardir)+"/config.json")
        with open(JSON_FILE_PATH,"r") as config_file:
            json_data = json.load(config_file)
        json_data = eval(json.dumps(json_data))
        return json_data
    except:
        return None