import csv
from datetime import datetime


def write_file():
    with open("notepad.csv", mode="a", encoding='utf-8') as w_file, open("notepad.csv", mode="r", encoding='utf-8') \
            as r_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        # считаем строки
        count = 2
        file_reader = csv.DictReader(r_file, delimiter=";")
        for row in file_reader:
            count += 1
        #date
        current_date_time = datetime.now()
        title = input("Введите заголовок: ")
        note = input("Введите заметку: ")
        file_writer.writerow([str(count), title, note, current_date_time])


