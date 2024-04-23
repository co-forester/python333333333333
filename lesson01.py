"""
1) написати програму яка вибирає зі введеної строки цифри та виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка
2,3,5,4,4 #вивело в консолі.
"""

print(', '.join([i for i in (input("Введіть рядок: ")) if i.isdigit()]))


"""
 *****************************************************************
2) написати прогу яка вибирає зі введеної строки числа і виводить їх
так як вони написані
наприклад:
st = 'as 23 fdfdg544 34' #введена строка
23, 544, 34              #вивело в консолі
"""

def choose_numbers(stri):
    numbers = []
    current_number = ''
    for i in stri:
        if i.isdigit():
            current_number += i
        elif current_number:
            numbers.append(current_number)
            current_number = ''
    if current_number:
        numbers.append(current_number)
    return ', '.join(numbers)


print(choose_numbers(input("Введіть рядок: ")))

# *****************************************************************
# list comprehension

# 1) є строка:
greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

print([i.upper() for i in greeting])

# *****************************************************************
# 2) з діапазону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрата
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

print([num ** 2 for num in range(51) if num % 2 != 0])


# *****************************************************************
# function

# - створити функцію яка виводить ліст
def display_list(list):
    print(list)


list = [1, 2, 3, 4, 5]
display_list(list)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def number_max(a, b, c):
    num_max = max(a, b, c)
    print("Найбільше число:", num_max)
    return num_max


number_max(10, 20, 15)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def min_max(*numbers):
    num_min = min(numbers)
    num_max = max(numbers)
    print("Найбільше число:", num_max)
    return num_min


min_max(5, 2, 8, 1, -3)


# - створити функцію яка повертає найбільше число з листа
def max_num(list):
    num = max(list)
    return num


list = [1, 2, 3, 4, 5]
print("Найбільше число в списку:", max_num(list))


# - створити функцію яка повертає найменьше число з листа
def min_num(list):
    num = min(list)
    return num


list = [1, 2, -3, 4, -5]
print("Найменьше число в списку:", min_num(list))


# - створити функцію яка приймає лист чисел та складає значення елементів листа та повертає його.
def sum_list(list):
    sum_l = sum(list)
    return sum_l


lll = [11, 2, 33, 4, 5]
print("Сума елементів списку:", sum_list(lll))


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def amg(list):
    arithmetic_mean = sum(list) / len(list)
    return arithmetic_mean


num_list = [1, 2, 3, 4, 5]
print("Середнє арифметичне значень списку:", amg(num_list))

# 1)Дан list:
list03 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


# - знайти мінімальне число
def find_min_from_list(list):
    print('min number = ', min(list))


# - видалити усі дублікати
def remove_duplicates(list):
    print(set(list))


# - замінити кожне 4-те значення на 'X'
def to_x(list):
    for i in range(3, len(list), 4):
        list[i] = 'X'
    print(list)


# 2) вивести на екран empty квадрат з "*" сторона якого вказана як агрумент функції
def empty_sq(d):
    for row in range(d):
        for column in range(d):
            if row == 0 or row == d - 1 or column == 0 or column == d - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


empty_sq(int(input('Введіть сторону квадрата:')))

empty_sq(6)  # Приклад для квадрата зі стороною 6


# 3) вивести табличку множення за допомогою циклу while
def tub_mult(rows, columns):
    row = 1
    while row <= rows:
        column = 1
        while column <= columns:
            print(row * column, end='\t')
            column += 1
        print()
        row += 1


tub_mult(9, 9)  # Таблиця множення 9x9

# 4) переробити це завдання під меню

while True:
    print('  1) Знайти min число')
    print('  2) Видалити дублікати')
    print('  3) Замінити кожне 4-те на X')
    print('  4) Вивести квадрат')
    print('  5) Вивести табличку множення')
    print('  9) Вихід')

    choice = input(" Зробіть свій вибір: ")

    if choice == '1':
        find_min_from_list(list03)
    elif choice == '2':
        remove_duplicates(list03)
    elif choice == '3':
        to_x(list03)
    elif choice == '4':
        empty_sq(int(input('Введіть сторону квадрата:')))
    elif choice == '5':
        tub_mult(9, 9)
    elif choice == '9':
        break
#***************************************************
print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='')
print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='-', end='')
print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='*', end='')
print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='\t ', end=' ')
print(isinstance(True, float))

lot = ['a', 'd', 'f', 'r', 'a']
print(lot[:3])
print(lot.count('a'))


imei = 863586055661569



