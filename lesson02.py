from typing import Callable, List, Tuple

#1)написати функцію на замикання котра буде в собі зберігати список справ,
#вам потрібно реалізувати два методи:
#- перший записує в список нову справу
#- другий повертає всі записи
def create_todo_list():
    todo_list = []

    def add_task():
        todo = input('впишіть нагадування: ')
        todo_list.append(todo)

    def get_tasks():
        return todo_list

    return add_task, get_tasks

# Приклад:
add_task, get_tasks = create_todo_list()

while True:
    print('щоб додати завдання натисніть 1')
    print('щоб вивести список завдань натисніть 2')
    print('якщо бажаєте закінчити натисніть 6 ')

    choice = input(" Зроби свій вибір: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        print("Список справ:", get_tasks())
    elif choice == '6':
        break

# 2) протипізувати перше завдання
def create_todo_list02() -> Tuple[Callable[[str], None], Callable[[], List[str]]]:
    todo_list: List[str] = []

    def add_todo(todo: str) -> None:
        todo_list.append(todo)

    def get_all() -> List[str]:
        return todo_list

    return add_todo, get_all

# Приклад:
add_todo, get_all = create_todo_list02()

add_todo("Поцілувати Оксану")
add_todo("Поцілувати Дашу")
add_todo("Вивчити python")
add_todo("Відпочити")

print("Список справ:", get_all())

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки
# (також використовуемо типізацію)
def expanded_form(number: int) -> str:
    num_str = str(number)
    result = []

    for i, digit in enumerate(num_str):  # ітератор
        if digit != '0':
            result.append(digit + '0' * (len(num_str) - i - 1))

    return ' + '.join(result)

# Приклад:
print(expanded_form(12))    # Виводить: '10 + 2'
print(expanded_form(42))    # Виводить: '40 + 2'
print(expanded_form(70304))  # Виводить: '70000 + 300 + 4'

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція,
# продекорована цим декоратором, та буде виводити це значення після виконання функцій
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        result = func(*args, **kwargs)
        print("Функція була викликана", wrapper.calls, "разів")
        return result
    wrapper.calls = 0
    return wrapper

# Приклад:
@count_calls
def greet(name):
    print("Привіт,", name, "!")

greet("Оксана")
greet("Сергій")
greet("Данііл")










