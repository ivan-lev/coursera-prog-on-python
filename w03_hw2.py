import os, csv

empty = ''

csv_filename = 'e:\Python\coursera-prog-on-python\coursera-prog-on-python\coursera_week3_cars.csv'

class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        file_name_ext = os.path.splitext(self.photo_file_name)
        return file_name_ext[1]


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_length, body_width, body_height):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.body_whl = body_whl
        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def whl_split(self, body_whl):
        if body_whl == '':
            pass
        else:
            characteristics = body_whl.split('x')
            body_length = float(characteristics[0])
            body_width = float(characteristics[1])
            body_height = float(characteristics[2])

    def get_body_volume(self):
        return body_length * body_width * body_height

        #Для грузового автомобиля необходимо разделить характеристики кузова на отдельные составляющие body_length, body_width, body_height. Разделитель — латинская буква x. Характеристики кузова могут быть заданы в виде пустой строки, в таком случае все составляющие равны 0. Обратите внимание на то, что характеристики кузова должны быть вещественными числами.
        #Также для класса грузового автомобиля необходимо реализовать метод get_body_volume, возвращающий объем кузова в метрах кубических.


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, car_type, extra):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.extra = extra
        self.car_type = car_type



def get_car_list(csv_filename):
    car_list = []
    object_list = []
    with open(csv_filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row != []:
                if row[0] != '':
                    car_list.append(row)
        for car in car_list:
            print(car)
    #далее мы напишем код, который берёт данные из car_list и на их основе создаёт
    #объекты в списке object_list, затем функция get_car_list возвращает этот список
    for car in car_list:
        if len(car) < 7:
            continue
        else:
            if
    return car_list


get_car_list(csv_filename)

a = []
a.append(SpecMachine('brand', 'photo_file_name', 'carrying', 'car_type', 'extra'))
print(a)
