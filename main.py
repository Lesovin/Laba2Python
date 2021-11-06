import json
import argparse
import os
from tqdm import tqdm


class ReadFromFile:
    def __init__(self, path: str):
        self.__data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self):
        return self.__data


parser = argparse.ArgumentParser(description='main')
parser.add_argument('-input', dest="file_input", default='69.txt', type=str)
parser.add_argument('-output', dest="file_output", default='69_output.txt', type=str)
args = parser.parse_args()
file = ReadFromFile(args.file_input)
output = open(args.file_output, 'w')
