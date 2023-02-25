import json

numbers = input("Введите заголовок \n")

filename = 'numbers.json'
with open(filename, 'a',  encoding='utf-8') as f_obj:
    json.dump(numbers, f_obj, ensure_ascii=False)
    f_obj.write('\n')
