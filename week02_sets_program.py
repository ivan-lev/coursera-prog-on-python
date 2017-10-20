import random

the_set = set()
k = 0

while True:
    x = random.randint(1, 10)
    if x not in the_set:  
        the_set.add(x)
        k += 1
    else:
        break

print('Функция random.randint(1, 10) выдала повтор через {} итераций'.format(k))
print(the_set)
print(repr(the_set))
