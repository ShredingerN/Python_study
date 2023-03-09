'''
Задача 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

'''


def calculator():
    oper = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if oper == '0':
        return 'Работа программы завершена'

    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))

    if oper == '+':
        print(f'{num_1 + num_2}')
        return calculator()
    if oper == '-':
        print(f'{num_1 - num_2}')
        return calculator()
    if oper == '*':
        print(f'{num_1 * num_2}')
        return calculator()
    try:
        if oper == '/':
            print(f'{num_1 / num_2}')
            return calculator()
    except ZeroDivisionError:
        print('На 0 делить нельзя!')
        calculator()
    else:
        print('Неверный символ операции!')
        return calculator()


print(calculator())
