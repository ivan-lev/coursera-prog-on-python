import random
a = sorted([random.randint(10, 20) for i in range(random.randint(10, 15))])
print(a)
half = len(a) // 2
print("len = ", len(a))
mediana = (a[half]) if len(a) % 2 != 0 else (a[half] + a[half - 1]) / 2
print(mediana)
