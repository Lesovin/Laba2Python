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


def serialization(database: list, path: str) -> None:
    with open(path, 'wb') as file:
        pickle.dump(database, file)


def deserialization(path: str) -> list:
    with open(path, 'rb') as file:
        database = pickle.load(file)
    return database
