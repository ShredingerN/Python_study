"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

"""
list_words = ['разработка', 'сокет', 'декоратор']

for el in list_words:
    print(
        f'тип переменной: {type(el)}, содержание:  {el}')

for el in list_words:
    f = el.encode('unicode_escape').decode('utf-8')
    print(
        f'тип переменной: {type(f)}, содержание:  {f}')
