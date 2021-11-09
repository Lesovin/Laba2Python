import json
import argparse
import re
from tqdm import tqdm


class ReadFromFile:
    """
    Объект класса ReadFromFile считывает и хранит данные из выбранного файла.

    Attributes
      ----------
      __data - хранит данные, считанные из файла
    """

    __data: object

    def __init__(self, path: str):
        """
        __init__ - инициализирует экземпляр класса ReadFromFile
        Parameters
        ----------
        path : str
        Путь до выбранного файла
        """
        self.__data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self) -> object:
        """
        data - метод получения данных файла
        :return: object
        """
        return self.__data


class Validator:
    __email: str
    __weight: int
    __inn: str
    __passport_series: str
    __university: str
    __age: int
    __political_views: str
    __worldview: str
    __address: str

    def __init__(self, email: str, weight: int, inn: str, passport_series: str, university: str, age: int,
                 political_views: str, worldview: str,
                 address: str):
        self.__email = email
        self.__weight = weight
        self.__inn = inn
        self.__passport_series = passport_series
        self.__university = university
        self.__age = age
        self.__political_views = political_views
        self.__worldview = worldview
        self.__address = address

    def check_email(self) -> bool:
        """
        Выполняет проверку корректности адреса электронной почты.

        Если в строке присутствуют пробелы, запятые, двойные точки,
        а также неверно указан домен адреса, то будет возвращено False.

        :return: bool
        Булевый результат проверки на корректность
        """
        if re.match(r"\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}", self.__email) is None:
            return False
        return True

    def check_weight(self) -> bool:
        if re.match(r"\b\d{2,3}\b", str(self.__weight)) is not None and (self.__weight > 30) and (self.__weight < 250):
            return True
        return False

    def check_age(self) -> bool:
        if re.match(r"\b\d{2,3}\b", str(self.__weight)) is not None and (self.__age > 18) and (self.__age < 122):
            return True
        return False

    def check_inn(self) -> bool:
        if len(self.__inn) == 12 and re.match(r"\d+", self.__inn) is not None:
            return True
        return False

    def check_passport_series(self) -> bool:
        if len(self.__passport_series) == 5 and re.match(r"\d{2}\s\d{2}", self.__passport_series) is not None:
            return True
        return False

parser = argparse.ArgumentParser(description='main')
parser.add_argument('-input', dest="file_input", default='69.txt', type=str)
parser.add_argument('-output', dest="file_output", default='69_output.txt', type=str)
args = parser.parse_args()
file = ReadFromFile(args.file_input)
output = open(args.file_output, 'w')

output.close()
