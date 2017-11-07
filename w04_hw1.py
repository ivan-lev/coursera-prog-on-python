'''
В этом задании вам нужно создать интерфейс для работы с файлами.
Класс File должен поддерживать несколько необычных операций.
1. Класс инициализируется полным путем.
2. Класс должен поддерживать метод write.
3. Объекты типа File должны поддерживать сложение.
    В этом случае создается новый файл и файловый объект, в котором содержимое
    второго файла добавляется к содержимому первого файла.
    Новый файл должен создаваться в директории, полученной с помощью
    tempfile.gettempdir. Для получения нового пути можно использовать os.path.join.
4. Объекты типа File должны поддерживать протокол итерации, причем итерация проходит по строкам файла.
5. При выводе файла с помощью функции print должен печататься его полный путь, переданный при инициализации.
'''

import os, tempfile

class File:
    def __init__(self, full_file_name):
        self.full_file_name = full_file_name
        self.current, self.end = 0, 0
        if not os.path.exists(full_file_name):
            with open(self.full_file_name, 'w') as f:
                pass
        # счётчик для итерации, начинается с нуля, заканчивается номером последней строки
        with open(self.full_file_name, 'r') as f:
            file_content = f.readlines()
            self.end = len(file_content)
            #print('File content is {}, self.end is {}'.format(file_content, self.end))

    def __str__(self):
        return self.full_file_name

    def __add__(self, added_file):
        result1, result2 = [], []
        fullpath = os.path.join(tempfile.gettempdir(), 'newfile.txt')
        with open(self.full_file_name, 'r') as f1, open(added_file.full_file_name, 'r') as f2:
            result1, result2 = f1.readlines(), f2.readlines()
        with open(fullpath, 'w') as f:
            f.writelines(result1)
            f.write('\n')
            f.writelines(result2)
        return File(fullpath)

    def write(self, what_write):
        with open(self.full_file_name, 'w') as f:
            f.write(what_write)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        with open(self.full_file_name, 'r') as f:
            all_lines = f.readlines()
            result = all_lines[self.current].strip()
        self.current += 1
        return result



#проверяем, что если файла нет, то он создастся
#non_existing_file = File(r'e:\Python\coursera-prog-on-python\coursera-prog-on-python\file!!!.txt')

#создаём экземпляр, проверяем его атрибуты, проверяем метод str, проверяем метод write
#obj = File(r'e:\Python\coursera-prog-on-python\coursera-prog-on-python\file.txt')
#print(obj.__dict__)
#print(obj)
#obj.write('line\n')

#проверяем сложение
first = File(r'e:\Python\coursera-prog-on-python\coursera-prog-on-python\file1.txt')
second = File(r'e:\Python\coursera-prog-on-python\coursera-prog-on-python\file2.txt')
new_obj = first + second

#проверяем итерацию
for line in new_obj:
    print(line)
