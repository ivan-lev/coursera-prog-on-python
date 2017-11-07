'''
Часто при зачислении каких-то средств на счет с нас берут комиссию.
Давайте реализуем похожий механизм с помощью дескрипторов.
Напишите дескриптор Value, который будет использоваться в нашем классе Account.

У аккаунта будет атрибут commission.
Именно эту коммиссию и нужно вычитать при присваивании значений в amount.
'''


class Value:
    def __init__(self):
        self.value = None

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        #здесь самый важный момент программы
        #мы берем значение коммиссии из obj
        self.value = value - value * obj.commission

class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)
#90
