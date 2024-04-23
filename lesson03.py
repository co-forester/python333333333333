from abc import ABC, abstractmethod
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
        self.area = x * y

    # def area(self):
    #     return self.x * self.y

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return abs(self.area - other.area)

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return not self.area == other.area

    def __gt__(self, other):
        return self.area > other.area

    def __lt__(self, other):
        return self.area < other.area

    def __len__(self):
        return self.x + self.y

# Приклад використання класу Rectangle:
rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 6)
rect3 = Rectangle(8, 7)

# print("Площа першого прямокутника:", rect1.area)   # 20
# print("Площа другого прямокутника:", rect2.area)   # 18
print("Сума площин двох прямокутників:", rect1 + rect2)   # 38
print("Різниця площин двох прямокутників:", rect1 - rect2)   # 2
print("Чи рівні площини двох прямокутників:", rect1 == rect2)   # False
print("Чи нерівні площини двох прямокутників:", rect1 != rect2)  # True
print("Перший прямокутник більший за другий:", rect1 > rect2)   # True
print("Перший прямокутник меншій за другий:", rect1 < rect2)   # False
print("Сума сторін першого прямокутника:", len(rect1))   # 9
print("Сума сторін другого прямокутника:", len(rect2))   # 9
print("Сума сторін іншого прямокутника:", len(rect3))   # 15

"""створити клас Human (name, age)
створити два класи Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір ноги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, 
та шукати ту саму

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
cinderella4 = Cinderella("Даша", 20, 35)
cinderellas = [cinderella4, cinderella1, cinderella2, cinderella3]

print('-' * 39)
print('-' * 39)
Cinderella.show_count()   # 4

prince = Prince("Олександр", 30, 35)
# prince.find_cinderella([cinderella1, cinderella2, cinderella3])   # Знайдена попелюшка: Анна
prince.find_cinderella(cinderellas)   # Знайдена попелюшка: Даша

"""1) Створити абстрактний клас Printable якій буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та якій наслідується від класу Printable
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом 
Book або Magazine інакше ігнорувати додавання
- метод show_all_magazines якій буде виводити всі журнали викликаючи метод print абстрактного класу
- метод show_all_books якій буде виводити всі книги викликаючи метод print абстрактного класу

Приклад:

Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))

    Main.show_all_magazines()
    print('-' * 40)
    Main.show_all_books()
    

для перевірки класів використовуємо метод isinstance, приклад:


user = User('Max', 15)
shape = Shape()

isinstance(max, User) -> True
isinstance(shape, User) -> False"""

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Книга: {self.name}")

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Журнал: {self.name}")

class Main:
    printable_list = []

    @classmethod
    def add(cls, item):
        if isinstance(item, (Book, Magazine)):
            cls.printable_list.append(item)
        else:
            print("Помилка: Можна додавати лише книги та журнали")

    @classmethod
    def show_all_magazines(cls):
        print("Всі журнали:")
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        print("Всі книги:")
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()

# Приклад використання:
Main.add(Magazine('Журнал 1'))
Main.add(Book('Книга 1'))
Main.add(Magazine('Журнал 2'))
Main.add(Magazine('Журнал 3'))
Main.add(Book('Книга 2'))
Main.add(Book('Книга 3'))
Main.add(Book('Книга 4'))

print('-' * 39)
print('-' * 39)
Main.show_all_magazines()
print('-' * 39)
Main.show_all_books()
print('-' * 39)
