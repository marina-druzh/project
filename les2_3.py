seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
         "ноябрь", "декабрь"]
month = input('Введите месяц числом от 1 до 12: ')
if month.isdigit() and 0 < int(month) <= 12:
    for key in seasons.keys():
        if int(month) in seasons[key]:
            print(f"Время года - {key}, месяц - {months[int(month) - 1]}")
else:
    print('Error!')


