"""Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
+ сумма площин двох екземплярів ксласу
- різниця площин двох екземплярів ксласу
== площин на рівність
!= площин на не рівність
>, < меньше більше
при виклику метода len() підраховувати сумму сторін"""
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return abs(self.area() - other.area())

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __len__(self):
        return self.x + self.y

# Приклад використання класу Rectangle:
rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 6)

print("Площа першого прямокутника:", rect1.area())   # 20
print("Площа другого прямокутника:", rect2.area())   # 18
print("Сума площин двох прямокутників:", rect1 + rect2)   # 38
print("Різниця площин двох прямокутників:", rect1 - rect2)   # 2
print("Чи рівні площини двох прямокутників:", rect1 == rect2)   # False
print("Чи нерівні площини двох прямокутників:", rect1 != rect2)  # True
print("Перший прямокутник більший за другий:", rect1 > rect2)   # True
print("Перший прямокутник менший за другий:", rect1 < rect2)   # False
print("Сума сторін першого прямокутника:", len(rect1))   # 9
print("Сума сторін другого прямокутника:", len(rect2))   # 9

        