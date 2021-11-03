
import json
from tqdm import tqdm


class ReadFromFile:
    def __init__(self, path: str):
        self.__data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self):
        return self.__data
