import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = int((-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a)
    x2 = int((-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a)
elif d == 0:
    x1 = x2 = int(-(b / (2 * a)))
else:
    x1 = x2 = None
    print('Корней на множестве действительных чисел нет.')
print(x1, x2, sep = '\n')
