'''
print(1/0)

class MyClass:
    pass
obj = MyClass
obj.foo

d = {'foo': 1}
d['bar']

l = [1, 2]
l[10]

int('line')


try:
    1 / 0
except:
    print("Ошибка")

#
while True:
    try:
        raw = input("введите число: ")
        number = int(raw)
    except ValueError:
        print("некорректное значение!")
    except KeyboardInterrupt:
        print("выход")
        break
    else:
        print('Вы ввели число')
        break
        
#
try:
    with open("/file/not/found") as f:
        content = f.read()
except OSError as err:
    print(err.errno, err.strerror)
'''
# атрибут args
import os.path

filename = "/file/not/found"
try:
    if not os.path.exists(filename):
        raise ValueError("файл не существует", filename)
except ValueError as err:
    message, code = err.args[0], err.args[1]
    print('Печатаем через блок except:', message, code)
