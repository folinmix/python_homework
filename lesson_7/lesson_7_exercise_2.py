""" Exercise 2
        Реализовать проект расчета суммарного расхода ткани на производство одежды.
        Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
        К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
        размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

        Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
        для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

        Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
        реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothing:

    def __init__(self, name: str):
        self.name = name
        self.square = 0


class Coat(Clothing):

    def __init__(self, name: str, parameter: [int, float]):
        super().__init__(name)
        self.size = parameter

    @property
    def get_area(self):
        self.square = round(self.size / 6.5 + 0.5, 2)
        return self.square


class Costume(Clothing):

    def __init__(self, name: str, parameter: [int, float]):
        super().__init__(name)
        self.height = parameter

    @property
    def get_area(self):
        self.square = round(self.height / 2 + 0.3, 2)
        return self.square


coat_1 = Coat("Spring", 170)
print(f'Площадь ткани для пальто {coat_1.name} = {coat_1.get_area}')
coat_2 = Coat("Winter", 150)
print(f'Площадь ткани для пальто {coat_2.name} = {coat_2.get_area}')
costume_1 = Costume("Nika", 170)
print(f'Площадь ткани для костюма {costume_1.name} = {costume_1.get_area}')
costume_2 = Costume("University", 150)
print(f'Площадь ткани для костюма {costume_2.name} = {costume_2.get_area}')

full_area = round(coat_1.get_area + coat_2.get_area + costume_1.get_area + costume_2.get_area, 2)
print(f'Общая площадь ткани для выбранной одежды = {full_area}')
