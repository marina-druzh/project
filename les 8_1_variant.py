class Data:
    date = 0
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


    @classmethod
    def extract(cls, day_month_year):
        try:

            my_date = str(day_month_year).split('-')
            date = [(int(my_date[i])) for i in range(len(my_date))]
            day, month, year = map(int, date)
            return cls(day, month, year)
        except ValueError:
            return 'Дата введена неверно'

    @staticmethod
    def check(obj):
        day = obj.day
        month = obj.month
        year = obj.year
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2099 >= year >= 0:
                    valid_date = '.'.join(map(str, [day, month, year]))
                    return f'Дата задана верно!: {valid_date}'
                else:
                    return f'Неверно задан год'
            else:
                return f'Неверно задан месяц'
        else:
            return f'Неверно задан день'

    def __str__(self):
        return f'Введена дата: {self.day, self.month, self.year}'



today = Data.extract('11 - 12 -2001')
print(Data.check(today))
print(today)
print(Data.check(Data.extract('33-05 - 897')))
print(Data.check(Data.extract('33-05 - 3343434')))
print(Data.extract('33-05 2020'))





