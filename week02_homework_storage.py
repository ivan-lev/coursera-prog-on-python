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

print(my_key)
print(my_value)

if my_value == None:
    with open('storage.txt', 'r') as f:
        database = {}
        for line in f:                      #считываем построчно файл и разделяем его
            temp_line = line.split()
            if temp_line[0] not in database: #если ключа нет в словаре database - добавляем его списком
                database[temp_line[0]] = [temp_line[1]]
            else:
                new_value = database.get(temp_line[0])  #иначе дергаем список, добавляем туда value 
                new_value.append(temp_line[1])          #и перезаписываем список по ключу
                database[temp_line[0]] = new_value
        value_list = database.get(my_key)
        for value in value_list:
            print(value, end = ' ')

else:
    # заносим в хранилище данные по ключу
    pass


#storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#with open(storage_path, 'w') as f:
#    pass
