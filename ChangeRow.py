import csv
from datetime import datetime


def change_row():
    with open("notepad.csv", mode="a", encoding='utf-8') as w_file, open("notepad.csv", mode="r", encoding='utf-8') \
            as r_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        # считаем строки
        count = 1
        file_reader = csv.DictReader(r_file, delimiter=";")
        changing_row = input("Введите номер строки для редактирования: ")
        for row in file_reader:
            if row[0] == changing_row:
                print(row)
                # current_date_time = datetime.now()
                # title = input("Введите заголовок: ")
                # note = input("Введите заметку: ")
                # file_writer.writerow([str(count), title, note, current_date_time])
            else:
                file_writer.writerow(row)
            count += 1


