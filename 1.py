class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extractor(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def valid(date_int):
        day, month, year = Date.extractor(date_int)
        if 2099 >= year <= 1900 or 12 > month < 1 or 1 > day > 31:
            return print('Не верная дата')
        elif month in (4, 6, 9, 11) and day > 30:
            return print('Не верная дата')
        elif (year % 400 != 0 and (year % 4 != 0 and year % 100 != 0)) and month == 2 and day > 28:
            return print('Не верная дата')
        else:
            return print('Верная дата')


print(Date.extractor('15-12-2019'))
Date.valid('32-11-2019')