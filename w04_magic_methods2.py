#encoding:  cp1251
class GetSet:
    def __init__(self, the_list):
        self.the_list = the_list

    def __getitem__(self, index):
        print('Вы обратились к элементу с порядковым номером ', index + 1, '. Его индекс = ', index)
        return(self.the_list[index])

    def __setitem__(self, index, value):
        print('Вы присвоили элементу с индексом ', index, 'значение ', value)
        self.the_list[index] = value

example = GetSet(['Calculator', 'Mouse', 'Keyboard', 'Monitor', 'Usb-hub'])
print(example[2])
example[3] = 'Stylus'
