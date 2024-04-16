# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

print(', '.join([i for i in (input("Введіть рядок: ")) if i.isdigit()]))


# *****************************************************************
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34' #введена строка
# 23, 544, 34              #вивело в консолі

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

# 1)є строка:
greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

print([i.upper() for i in greeting])

# *****************************************************************
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
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

# - створити функцію яка повертає найбільше число з ліста
def max_num(list):
    num = max(list)
    return num

list = [1, 2, 3, 4, 5]
print("Найбільше число в списку:", max_num(list))
# - створити функцію яка повертає найменьше число з ліста
def min_num(list):
    num = min(list)
    return num

list = [1, 2, -3, 4, -5]
print("Найменьше число в списку:", min_num(list))
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_list(list):
    sum_l = sum(list)
    return sum_l

lll = [11, 2, 33, 4, 5]
print("Сума елементів списку:", sum_list(lll))
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне йогоно значень.
def amg(list):
    arithmetic_mean = sum(list) / len(list)
    return arithmetic_mean

num_list = [1, 2, 3, 4, 5]
print("Середнє арифметичне значень списку:", amg(num_list))

# 1)Дан list:
list03 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# - знайти мін число
print('min number = ', min(list03))
# - видалити усі дублікати
print(set(list03))
# - замінити кожне 4-те значення на 'X'
for i in range(3, len(list03), 4):
    list03[i] = 'X'
print(list03)


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def empty_sq(d):
    for row in range(d):
        for column in range(d):
            if row == 0 or row == d - 1 or column == 0 or column == d - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()



# empty_sq(input("Введіть сторону квадрата: "))


empty_sq(6)  # Приклад для квадрата зі стороною 6

# 3) вывести табличку множення за допомогою цикла while
def tub_mult(rows, columns):
    row = 1
    while row <= rows:
        column = 1
        while column <= columns:
            print(row * column, end='\t')
            column += 1
        print()
        row += 1

tub_mult(10, 10)  # Таблиця множення 10x10


# 4) переробити це завдання під меню

# ????????

