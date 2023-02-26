import csv
from datetime import datetime

with open("classmates.csv", mode="a", encoding='utf-8') as w_file:

    file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
    current_date_time = datetime.now()
    file_writer.writerow(["Заголовок", "Заметка", "Дата"])
    title = input("Введите заголовок: ")
    note = input("Введите заметку: ")
    file_writer.writerow([title, note, current_date_time])


