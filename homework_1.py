from datetime import datetime
import random
import re

# функція розраховує кількість днів між заданою датою і поточною датою
def get_days_from_today(date):
    # перевірка формату вхідних даних
    try:
        date_users = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print(f"Invalid date format: {date}. There must be: YYYY-MM-DD")
        return()                          #якщо формат неправильний повертається пусте значення та повідомлення
    date_current = datetime.today().date()                                  #отримання поточної дати
    difference_date = (date_users.toordinal() - date_current.toordinal())   #різниця між датами в днях
    return (difference_date)

# функція генерує випадковий набір чисел у межах заданих параметрів: 
# (мінімальне, максимальне можливе число та кількість чисел, які потрібно вибрати)
def get_numbers_ticket(min, max, quantity):
    numbers_ticket = list()
    # перевірка відповідності вхідних параметрів заданим обмеженням
    # у разі невідповідності повертається порожній список
    if not ((1 <= min <= 1000) and (1 <= max <= 1000) and (min < max) and (0 < quantity <= (max - min))):
        return(numbers_ticket)
    i = 1
    while i <= quantity:
        number = random.randint(min, max)       # отримання випадкового числа
        if numbers_ticket.count(number) == 0:   # перевірка на унікальність числа серед уже одержаних
            numbers_ticket.append(number)       # додавання унікального випадкового числа
            i += 1
    numbers_ticket.sort()                       # сортировка вихідного списку
    return(numbers_ticket)

# функція нормалізує телефонні номери до стандартного формату
def normalize_phone(phone_number):
    result = re.findall(r'\d+', phone_number)   # видалення всіх символів, окрім цифр
    if result[0].startswith("0"):               # перевірка наявності міжнародного коду
        result[0] = '38' + result[0]            # додавання міжнародного коду у разі його відсутності
    new_string = '+' + ''.join(result)          # додавання "+" с початку номера
    return(new_string)



new_year_left = get_days_from_today('2025-01-01')
print(f'До Нового року залишилось {new_year_left} днів')

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

