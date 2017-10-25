'''
Week 2, home work 1
Program that can save key and values in the file and read
the data and print it if needed
'''

import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help="key that you want to store")
parser.add_argument("-v", "--value", help="value that you want to store for this key")

args = parser.parse_args()

my_key = args.key
my_value = args.value

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')



if my_value == None: # если my_value не задан, то формируем словарь и выводим данные по my_key
    if os.path.exists(storage_path) == False: # проверяем, есть ли файл, если не то создаём
        f = open(storage_path, 'w')
        f.close()
    else:
        with open(storage_path, 'r') as f:
            database = [] # создаём список значений для искомого ключа
            for line in f: #считываем построчно файл
                data = json.loads(line) # закидываем строку в словарь data
                #print(data)
                if my_key in data: # если ключ есть в проверяемой строчке
                    database.append(data.get(my_key)) # то заносим значение в database
            print(', '.join(database))
else:    # заносим в хранилище данные по ключу
    with open(storage_path, 'a') as f:
        f.write(json.dumps({my_key: my_value}) + '\n')
