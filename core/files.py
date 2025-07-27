from pathlib import Path
import json

class file_worker():
    file_data = []
    data_file_name = "config.json"
    fp = []

    def __init__(self):
        if Path(self.data_file_name).exists():
            self.fp = open(self.data_file_name)
        else:
            self.fp = open(self.data_file_name, "w")
            self._default_init()

        self.file_data = json.load(self.fp)

    def _default_init(self):
        self.fp = json.dumps({'dirs_array': ["audio"]})