def logger(filename):                       #2
    def decorator(func):                    #3
        def wrapped(*args, **kwargs):       #5
            result = func(*args, **kwargs)  #6
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator

@logger('new_log.txt')                      #1
def summator(num_list):                     #4
    return sum(num_list)

summator([1, 2, 3, 4, 5, 6])

with open('new_log.txt', 'r') as f:
    print(f.read())

'''
1. Применяем декоратор к сумматору
2. Вызывается функция logger, в которую передаём filename
3. logger возвращает decorator
4. decorator принимает функцию(в данном случае summator)
5. и возвращает новую функцию wrapped, которая подменяет наш summator
6. внутри функции wrapped вызывается исходная функция summator
   и записывается её результат в файл
'''
