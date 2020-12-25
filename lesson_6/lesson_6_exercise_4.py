""" Exercise 4
        Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
        speed, color, name, is_police (булево).
        А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
        остановилась, повернула (куда).
        Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
        Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
        Для классов TownCar и WorkCar переопределите метод show_speed.
        При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщениео превышении скорости.
        Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
        Выполните вызов методов и также покажите результат.
"""


class Car:
    __class_direction = {"straight": "едет прямо.",
                         "left": "повернул налево.",
                         "right": "повернул направо.",
                         "back": "развернулся."}
    __real_speed = 0

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.__real_speed = self.speed
        return f"{self.color} {self.name} начал движение."

    def stop(self):
        self.__real_speed = 0
        return f"{self.color} {self.name} остановился."

    def turn(self, direction: str):
        """
            Метод принимает одно из 4 значений (straight, left, right, back) в формате str
            :param direction: str
            :return: str
        """
        if not self.__real_speed:
            return f"{self.color} {self.name} стоит на месте. Для изменения направления нужно начать движение."
        else:
            if direction in self.__class_direction.keys():
                return f"{self.color} {self.name} {self.__class_direction[direction]}"
            else:
                print("Ошибка! Недопустимыйаргумент метода turn!")

    def show_speed(self):
        if not self.__real_speed:
            return f"{self.color} {self.name} не движется."
        else:
            return f"{self.color} {self.name} движется со скоростью {self.__real_speed}."


class TownCar(Car):
    __max_speed = 60

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if not self._Car__real_speed:
            return f"{self.color} {self.name} не движется."
        else:
            if self._Car__real_speed > self.__max_speed:
                return f"{self.color} {self.name} превысил скорость на {self._Car__real_speed - self.__max_speed}!"
            else:
                return f"{self.color} {self.name} движется со скоростью {self._Car__real_speed}."


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    __max_speed = 40

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if not self._Car__real_speed:
            return f"{self.color} {self.name} не движется."
        else:
            if self._Car__real_speed > self.__max_speed:
                return f"{self.color} {self.name} превысил скорость на {self._Car__real_speed - self.__max_speed}!"
            else:
                return f"{self.color} {self.name} движется со скоростью {self._Car__real_speed}."


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


my_list = ["- не полицейский автомобиль", "- полицейский автомобиль "]

# Create first police car
Police_Mersedes = PoliceCar(80, "Полицейский", "Мерседес", True)
print('\n----Первый полицейский автомобиль----')
print(f"{Police_Mersedes.color} {Police_Mersedes.name} {my_list[Police_Mersedes.is_police]}")
print(Police_Mersedes.show_speed())
print(Police_Mersedes.turn("straight"))
print(Police_Mersedes.go())
print(Police_Mersedes.turn("back"))
print(Police_Mersedes.show_speed())
print(Police_Mersedes.stop())
print(Police_Mersedes.show_speed())

# Create second police car
Police_Lexus = PoliceCar(50, "Полицейский", "Лексус", True)
print('\n----Второй полицейский автомобиль----')
print(f"{Police_Lexus.color} {Police_Lexus.name} {my_list[Police_Lexus.is_police]}")
print(Police_Lexus.show_speed())
print(Police_Lexus.turn("straight"))
print(Police_Lexus.go())
print(Police_Lexus.turn("left"))
print(Police_Lexus.show_speed())
print(Police_Lexus.stop())
print(Police_Lexus.show_speed())

# Create first town car
Red_Reno = TownCar(70, "Красный", "Рено", False)
print('\n----Первый городской автомобиль----')
print(f"{Red_Reno.color} {Red_Reno.name} {my_list[Red_Reno.is_police]}")
print(Red_Reno.show_speed())
print(Red_Reno.turn("straight"))
print(Red_Reno.go())
print(Red_Reno.turn("left"))
print(Red_Reno.show_speed())
print(Red_Reno.stop())
print(Red_Reno.show_speed())

# Create second town car
Black_Kia = TownCar(40, "Чёрный", "Киа", False)
print('\n----Второй городской автомобиль----')
print(f"{Black_Kia.color} {Black_Kia.name} {my_list[Black_Kia.is_police]}")
print(Black_Kia.show_speed())
print(Black_Kia.turn("straight"))
print(Black_Kia.go())
print(Black_Kia.turn("right"))
print(Black_Kia.show_speed())
print(Black_Kia.stop())
print(Black_Kia.show_speed())

# Create first sport car
White_BMW = SportCar(120, "Белый", "БМВ", False)
print('\n----Первый спортиный автомобиль----')
print(f"{White_BMW.color} {White_BMW.name} {my_list[White_BMW.is_police]}")
print(White_BMW.show_speed())
print(White_BMW.turn("straight"))
print(White_BMW.go())
print(White_BMW.turn("straight"))
print(White_BMW.show_speed())
print(White_BMW.stop())
print(White_BMW.show_speed())

# Create second sport car
Green_Corvet = SportCar(90, "Зелёный", "Корвет", False)
print('\n----Второй спортиный автомобиль----')
print(f"{Green_Corvet.color} {Green_Corvet.name} {my_list[Green_Corvet.is_police]}")
print(Green_Corvet.show_speed())
print(Green_Corvet.turn("straight"))
print(Green_Corvet.go())
print(Green_Corvet.turn("left"))
print(Green_Corvet.show_speed())
print(Green_Corvet.stop())
print(Green_Corvet.show_speed())

# Create first work car
Yellow_Track = WorkCar(60, "Жёлтый", "Трактор", False)
print('\n----Первый рабочий автомобиль----')
print(f"{Yellow_Track.color} {Yellow_Track.name} {my_list[Yellow_Track.is_police]}")
print(Yellow_Track.show_speed())
print(Yellow_Track.turn("straight"))
print(Yellow_Track.go())
print(Yellow_Track.turn("back"))
print(Yellow_Track.show_speed())
print(Yellow_Track.stop())
print(Yellow_Track.show_speed())

# Create second work car
Blue_Track = WorkCar(20, "Синий", "Трактор", False)
print('\n----Второй рабочий автомобиль----')
print(f"{Blue_Track.color} {Blue_Track.name} {my_list[Blue_Track.is_police]}")
print(Blue_Track.show_speed())
print(Blue_Track.turn("straight"))
print(Blue_Track.go())
print(Blue_Track.turn("right"))
print(Blue_Track.show_speed())
print(Blue_Track.stop())
print(Blue_Track.show_speed())

