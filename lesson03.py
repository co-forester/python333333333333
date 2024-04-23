"""Створити клас Rectangle:
-він має приймати дві сторони x, y
-описати поведінку на арифметичні методи:
+ сума площин двох екземплярів класу
- різниця площин двох екземплярів класу
== площин на рівність
!= площин на не рівність
>, < менше більше
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

"""створити клас Human (name, age)
створити два класи Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір ноги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму

в класі попелюшки має бути count якій буде зберігати кількість створених екземплярів класу
також має бути метод класу якій буде виводити це значення"""
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):
    count = 0

    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella.count += 1

    @classmethod
    def show_count(cls):
        print("Кількість попелюшок:", cls.count)

class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, cinderellas):
        for cinderella in cinderellas:
            if cinderella.shoe_size == self.shoe_size:
                print("Знайдена попелюшка:", cinderella.name)
                return
        print("Попелюшка не знайдена")

# Приклад використання класів
cinderella1 = Cinderella("Анна", 20, 35)
cinderella2 = Cinderella("Марія", 22, 36)
cinderella3 = Cinderella("Ольга", 25, 34)

Cinderella.show_count()   # 3

prince = Prince("Олександр", 30, 35)
prince.find_cinderella([cinderella1, cinderella2, cinderella3])   # Знайдена попелюшка: Анна
        