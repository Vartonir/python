"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.

"""


# def func_data(name, surname, date_of_birth, city, email, tel_number):
#     return print(f'{name.title()} {surname.title()} родился в {date_of_birth} в городе {city.title()} \n'
#                  f'Контактные данные: \n'
#                  f'Электронная почта {email} \n'
#                  f'Номер телефона: {tel_number}')


# def func_data(name, surname, date_of_birth, city, email, tel_number):
#     return print(f'{name.title()} {surname.title()} родился в {date_of_birth} в городе {city.title()}'
#                  f' Контактные данные:'
#                  f' Электронная почта {email}'
#                  f' Номер телефона: {tel_number}'.title())
#
#
# func_data('василий')


def func_data2(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:  {value}.'.title())


func_data2(**{"Имя": 'василий', "Фамилия": 'рязанцев', "Дата рождения": 1978, "Город": 'воронеж',
              "email": 'v.ryazancev@mail.ru', "telephone": 9507511})
