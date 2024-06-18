import re

# функція нормалізує телефонні номери до стандартного формату
def normalize_phone(phone_number):
    result = re.findall(r'\d+', phone_number)   # видалення всіх символів, окрім цифр
    if result[0].startswith("0"):               # перевірка наявності міжнародного коду
        result[0] = '38' + result[0]            # додавання міжнародного коду у разі його відсутності
    new_string = '+' + ''.join(result)          # додавання "+" с початку номера
    return(new_string)


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