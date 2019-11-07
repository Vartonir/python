# Первое задание

# a = 47
# b = 'Первый шаг'
# c = 15.951
#
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
#
# number_entry = int(input('Введите число: '))
# text_entry = input('Введите текст: ')
# dro_entry = float(input('Введите дробное число: '))
#
# print(f'Ваше число {number_entry} ', type(number_entry))
# print(f'Ваш текст: {text_entry} ', type(text_entry))
# print(f'Ваше дробное число: {dro_entry} ', type(dro_entry))

# Второе задание

# time_seconds_entry = int(input("Введите время в секундах: "))
#
# time_hh = time_seconds_entry // 3600
# time_mm = time_seconds_entry % 3600 // 60
# time_ss = time_seconds_entry % 3600 % 60
#
# print(f'Получилось {time_hh}:{time_mm}:{time_ss}')

# Третье задание

# n = input('Введите число n: ')
#
#
# n_2 = int(n + n)
# n_3 = int(n + n + n)
# n = int(n)
#
# result = n + n_2 + n_3
# print(result)

# Четвёртое задание

# number_entry = int(input('Введите положительное число: '))
#
# while number_entry < 0:
#     number_entry = int(input('Введите только положительное число!! : '))
#
# m = number_entry % 10   # максимальное число
# b = number_entry // 10
#
# while b > 0:
#     if b%10 > m:
#         m = b%10
#     b = b // 10
#
# print('Максимальное цифра из числа ', m)


# Пятое задание

# prihod = int(input('Введите сумму выручки фирмы: '))
# rashod = int(input('Введите расход фирмы: '))
#
# if prihod > rashod:
#     print('Прибыль — выручка больше издержек')
#
#     people = int(input('введите число сотрудников: '))
#     pribyl = prihod - rashod
#     prihod_per_people = int(pribyl / people)
#     print(f'Прибыль на одного сотрудника: {prihod_per_people}')
# else:
#     print('убыток — издержки больше выручки')

# Шестое задание

a = 15
b = 50
n = 0

while a < b:
    a = a + a*0.1
    n = n + 1

print(n)






