import os, csv

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
    def __init__(self, car_type, brand, photo_file_name, carrying, body_width, body_height, body_length):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.body_width = body_width
        self.body_height = body_height
        self.body_length = body_length

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.extra = extra


def check_car_data(car):
    if car[0] == 'car' and car[1] != '' and car[2] != '' and car[3] != '' and car[5] != '':
        return True
    elif car[0] == 'truck' and car[1] != '' and car[3] != '' and car[5] != '':
        return True
    elif car[0] == 'spec_machine' and car[1] != '' and car[3] != '' and car[5] != '' and car[6] != '':
        return True
    else:
        return False


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
        if check_car_data(car) == False:
            continue
        else:
            car_brand = car[1]
            car_ps =  int(car[2]) if car[2] != '' else ''
            car_photo = car[3]
            car_whl = car[4]
            car_carry = float(car[5])
            car_extra = car[6]
            if car[0] == 'car':
                object_list.append(Car(car[0], car_brand, car_photo, car_carry, car_ps))
            elif car[0] == 'truck':
                if car[4] == '':
                    body_width, body_height, body_length = 0, 0, 0
                else:
                    body_whl = car[4].split('x')
                    body_width, body_height, body_length = float(body_whl[0]), float(body_whl[1]), float(body_whl[2])
                object_list.append(Truck(car[0], car_brand, car_photo, car_carry, body_width, body_height, body_length))
            elif car[0] == 'spec_machine':
                object_list.append(SpecMachine(car[0], car_brand, car_photo, car_carry, car_extra))
    return object_list


#csv_filename = 'e:\Python\coursera-prog-on-python\coursera-prog-on-python\coursera_week3_cars.csv'
#x = get_car_list(csv_filename)
#for i in x:
#    print(i.__dict__)

#answer = get_car_list(csv_filename)
#for i in answer:
#    print(i.__dict__)
