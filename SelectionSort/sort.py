import json
from tqdm import trange
import pickle


def read_data(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as rfile:
        database = json.load(rfile)
    return database


def selection_sort(database: list):
    for i in trange(len(database) - 1):
        for k in range(i + 1, len(database)):
            if database[k]['weight'] < database[i]['weight']:
                database[k], database[i] = database[i], database[k]


data = read_data("D:/PythonProjects/Laba2/69_output.txt")
selection_sort(data)
with open('69_sorted.txt', 'wb') as file:
    pickle.dump(data, file)
with open('69_sorted.txt', 'rb') as file:
    data = pickle.load(file)
print(data)
