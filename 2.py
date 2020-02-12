class MyException(Exception):
    def __init__(self):
        self.txt = 'Вы пытаетесь поделить на ноль'


try:
    a, b = map(int, input('Введите делимое и делитель через пробел ').split())
    if b == 0:
        raise MyException
except ValueError:
    print('Введены некорректные данные')
except MyException as err:
    print(err.txt)
else:
    print(a / b)