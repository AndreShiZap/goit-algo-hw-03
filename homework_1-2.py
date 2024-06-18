import random

# функція генерує випадковий набір чисел у межах заданих параметрів: 
# (мінімальне, максимальне можливе число та кількість чисел, які потрібно вибрати)
def get_numbers_ticket(min, max, quantity):
    numbers_ticket = list()
    # перевірка відповідності вхідних параметрів заданим обмеженням
    # у разі невідповідності повертається порожній список
    if not ((1 <= min <= 1000) and (1 <= max <= 1000) and (min < max) and (0 < quantity <= (max - min))):
        return(numbers_ticket)
    d_numbers_ticket = set(numbers_ticket)              # перетворення списку у множину 
    while len(d_numbers_ticket) < quantity:             # перевірка кількості чисел у множині
        d_numbers_ticket.add(random.randint(min, max))  # додавання випадкового числа у множину
    numbers_ticket = list(d_numbers_ticket)             # перетворення множини у список
    # другий варіант - без використання множини:    
    #i = 1
    #while i <= quantity:
    #    number = random.randint(min, max)       # отримання випадкового числа
    #    if numbers_ticket.count(number) == 0:   # перевірка на унікальність числа серед уже одержаних
    #        numbers_ticket.append(number)       # додавання унікального випадкового числа
    #        i += 1
    numbers_ticket.sort()                       # сортировка вихідного списку
    return(numbers_ticket)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)