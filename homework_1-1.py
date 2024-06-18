from datetime import datetime

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


new_year_left = get_days_from_today('2025-01-01')
print(f'До Нового року залишилось {new_year_left} днів')
