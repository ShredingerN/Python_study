'''
Задание 2.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

'''
number = int(input("Введите целое положительное число: "))
max_digit = number % 10
while number >= 1:
    number = number // 10
    rest = number % 10
    if rest > max_digit:
        max_digit = rest
print(f"Максимальное цифра: {max_digit}")

# вот здесь у меня возник ступор, без else оказалось работает))
# находила разные варианты кода, но я их для себя не объяснила