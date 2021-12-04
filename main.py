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
    __university_invalid = ['Каражан', 'Шармбатон', 'Бан Ард', 'Дурмстранг', 'Гвейсон Хайль', 'Кирин-Тор', 'Хогвартс',
                            'Аретуза', ]
    __worldview_invalid = ['Культ пророка Лебеды', 'Культ богини Мелитэле', 'Культ Механикус',
                           'Светское гачимученничество', 'Храм Трибунала', 'Девять божеств', 'Культ проклятых']
    __political_views_invalid = ['поддерживает Имперский легион',
                                 'согласен с действиями Гарроша Адского Крика на посту вождя Орды',
                                 'поддерживает Братьев Бури', 'патриот независимой Темерии', ]

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
        if re.match(r"\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}", self.__email) is not None:
            return True
        return False

    def check_weight(self) -> bool:
        """
        Выполняет проверку корректности записи веса.

        Если записано не двух- или трехзначное число, число не >30 или не <250, то возвращает False.
        Иначе True.
        :return: bool
        Булевый результат проверки на корректность
        """
        if re.match(r"\d{2,3}\b", str(self.__weight)) is not None and (int(self.__weight) > 30) and (
                int(self.__weight) < 250):
            return True
        return False

    def check_inn(self) -> bool:
        """
        Выполняет проверку корректности записи номера СНИЛСа.

        Если записано не число, и количество чисел не равно 12, то возвращает False.
        Иначе True.
        :return: bool
        Булевый результат проверки на корректность
        """
        if len(self.__inn) == 12 and re.match(r"\d+", self.__inn) is not None:
            return True
        return False

    def check_passport_series(self) -> bool:
        """
        Выполняет проверку корректности записи серии паспорта.

        Если записано не 5 знаков, или не записано два числа через пробел, то возвращает False.
        Иначе True.
        :return: bool
        Булевый результат проверки на корректность
        """
        if len(self.__passport_series) == 5 and re.match(r"\d{2}\s\d{2}", self.__passport_series) is not None:
            return True
        return False

    def check_university(self) -> bool:
        """
        Выполняет проверку корректности записи названия университета.

        Если записаны не буквы и университет входит в список несуществующих, то возвращает False.
        Иначе True.
        :return: bool
        Булевый результат проверки на корректность
        """
        if re.match(r"^[\D]+$", self.__university) is not None and self.__university not in self.__university_invalid:
            return True
        return False

    def check_age(self) -> bool:
        """
        Выполняет проверку корректности записи возраста.

        Если записано не двух- или трехзначное число, число не >18 или не <122, то возвращает False.
        Иначе True.
        :return: bool
        Булевый результат проверки на корректность
        """
        if re.match(r"\d{2,3}$", str(self.__age)) is not None and (int(self.__age) > 0) and (
                int(self.__age) < 122):
            return True
        return False

    def check_political_views(self) -> bool:
        """
        Выполняет проверку корректности записи политических взглядов.

        Если записаны не буквы или такие политические взгляды не существуют, то возвращает False.
        Иначе True.
        :return: bool
        Булевый результат проверки на корректность
        """
        if self.__political_views not in self.__political_views_invalid and re.match(r"^[\D]+$",
                                                                                     self.__worldview) is not None:
            return True
        return False

    def check_worldview(self) -> bool:
        """
        Выполняет проверку корректности записи мировоззрения.

        Если записаны не буквы, или такое мировоззрение не существует, то возвращает False.
        Иначе True.
        :return: bool
        Булевый результат проверки на корректность
        """
        if self.__worldview not in self.__worldview_invalid and re.match(r"^[\D]+$", self.__worldview) is not None:
            return True
        return False

    def check_address(self) -> bool:
        """
        Выполняет проверку корректности веса.

        Если название улицы не начинается с ул. или начинается с Алллея, то возвращает False.
        Иначе True.
        :return: bool
        Булевый результат проверки на корректность
        """
        if re.match(r"^(ул\.)?(Аллея)?\s[\w.\s-]+\d+$", self.__address) is not None:
            return True
        return False

    def check_all(self) -> int:
        if not self.check_email():
            return 0
        elif not self.check_weight():
            return 1
        elif not self.check_inn():
            return 2
        elif not self.check_passport_series():
            return 3
        elif not self.check_university():
            return 4
        elif not self.check_age():
            return 5
        elif not self.check_political_views():
            return 6
        elif not self.check_worldview():
            return 7
        elif not self.check_address():
            return 8
        else:
            return 9


parser = argparse.ArgumentParser(description='main')
parser.add_argument('-input', dest="file_input", default='69.txt', type=str)
parser.add_argument('-output', dest="file_output", default='69_output.txt', type=str)
args = parser.parse_args()
file = ReadFromFile(args.file_input)
output = open(args.file_output, 'w')
errors = [0, 0, 0, 0, 0, 0, 0, 0, 0]
number_of_valid_records = 0
data_to_write = []
with tqdm(file.data, desc='Прогресс валидации', colour="#FFFFFF") as progressbar:
    for elem in file.data:
        check = Validator(elem['email'], elem['weight'], elem['inn'], elem['passport_series'], elem['university'],
                          elem['age'], elem['political_views'], elem['worldview'], elem['address'])
        error = check.check_all()
        if error == 9:
            data_to_write.append(elem)
            number_of_valid_records += 1
        else:
            errors[error] += 1
        progressbar.update(1)
number_of_invalid_records = errors[0] + errors[1] + errors[2] + errors[3] + errors[4] + errors[5] + errors[6] + errors[
    7] + errors[8]
json.dump(data_to_write, output)
print("Общее число корректных записей:", number_of_valid_records, )
print("Общее число некорректных записей:", number_of_invalid_records)
print("Ошибки в email:", errors[0])
print("Ошибки в weight:", errors[1])
print("Ошибки в inn:", errors[2])
print("Ошибки в passport_series:", errors[3])
print("Ошибки в university:", errors[4])
print("Ошибки в age:", errors[5])
print("Ошибки в political_views:", errors[6])
print("Ошибки в worldview:", errors[7])
print("Ошибки в address:", errors[8])
output.close()
