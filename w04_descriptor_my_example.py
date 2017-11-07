
class NameDescriptor:
    def __init__(self, first_name):
        self.first_name = first_name
    
    def __get__(self, obj, obj_type):
        return self.first_name
    
    def __set__(self, obj, value):
        if value[0].islower():
            print('Имя должно начинаться с большой буквы')
            print('Мы запишем ваше имя с большой буквы')
            value = value.capitalize()
        self.first_name = value

    
class UserClass:
    first_name = NameDescriptor('default_name')
    last_name = NameDescriptor('default_name')

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
my_account = UserClass()
my_account.first_name = 'петя'
my_account.last_name = 'Егоров'

print('\nАтрибуты вашего экземпляра:\n', dir(my_account))
print('\nВаше имя {}, ваша фамилия {}'.format(my_account.first_name, my_account.last_name))
print(my_account.full_name)
