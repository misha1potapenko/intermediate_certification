import csv


class NotepadReader:
    def read_file(self):
        with open("notepad.csv", encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter = ";")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count == 0:
                    # Вывод строки, содержащей заголовки для столбцов
                    print(f'Файл содержит столбцы: {"; ".join(row)}')
                else:
                    # Вывод строк
                    print(f'Заголовок {row[0]}  Текст заметки {row[1]}  Дата {row[2]}')
                count += 1
            print(f'Всего в файле {count} строк.')
