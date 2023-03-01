import csv


def find_note():
    with open("notepad.csv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ";"
        file_reader = csv.reader(r_file, delimiter=";")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        what_find = input("Введите слово, которое будем искать: \n")
        for row in file_reader:
            if row[0] == what_find or row[1] == what_find:
                print("Найдена строка: ")
                print(f'Номер строки: {row[0]}; Заголовок: {row[1]};  Текст заметки: {row[2]};  Дата: {row[3]}')
                count += 1

        if count == 0:
            print("Запись не найдена")

