# file_reader.py

from pathlib import Path

class ReadFile:
    @staticmethod
    def read_file(file_path):
        contents = Path(file_path).read_text()
        return contents
