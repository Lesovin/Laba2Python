import json
import argparse
from SelectionSort import sort
from SelectionSort import validator
from tqdm import tqdm

parser = argparse.ArgumentParser(description='main')
parser.add_argument('-input', dest="file_input", default='D:/PythonProjects/Laba2/69.txt', type=str)
parser.add_argument('-output', dest="file_output", default='D:/PythonProjects/Laba2/69_output.txt', type=str)
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
