# Задание 3.
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.

n = input("Введите целое положительное число: ")
#делаем сцепление строк, и переводим их в числа
#т.е. n=5---> 5 + 55 + 555 => находим сумму полученных сложенных строк, переве
# денных в числа
sum_string = int(n) + int(n * 2) + int(n * 3)
#затем эти числа сцепляем как строки
print(f"{n}+{n * 2}+{n * 3} = {sum_string}")