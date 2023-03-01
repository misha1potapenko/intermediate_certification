import csv
from datetime import datetime
import os


def delite_row():
    with open("notepad.csv", mode="r", encoding='utf-8') as r_file, open("notepad1.csv", mode="a", encoding='utf-8') \
            as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        # считаем строки
        count = 1
        file_reader = csv.reader(r_file, delimiter=";")
        changing_row = input("Введите номер строки для удаления: ")
        for row in file_reader:
            if row[0] == changing_row:
                count += 1
            else:
                file_writer.writerow(row)
            count += 1
    os.remove('notepad.csv')
    os.replace('notepad1.csv', 'notepad.csv')