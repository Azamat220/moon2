"""Функции, аргументы: *args, **kwargs."""

# DRY - don't repeat yourself
# def - definite (определить)

# contacts = {
#     'sam': '0500100200',
#     'aza': '0700223311',
#     'uri': '0555788877'
# }

# def find_contact():
#
#
# def new_contact(name, phone):
#     if name not in contacts.keys():
#         contacts[name] = phone
#     else:
#         contacts[name] = {contacts[name]}
#         contacts[name].add(phone)
#
#
# def delete(value):
#     command = input('выберите удаление: 1)по имени 2) по номеру')
#     if command == '1':
#         if value in contacts.keys():
#             del contacts[value]
#         else:
#             print(f'нет такого контакта {value}')
#     if command == '2':
#         for name, phone in contacts.items():
#             if value == phone:
#                 del_contact = name
#         del contacts[del_contact]
#
# delete('0700223311')
#
# print(contacts)


# def calculator(n1, operator, n2):

# def menu(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     return kwargs
#
# menu(eat='pizza', drink='tea', one=1, book='lutz')


# def plus(a, *args,  b=30):
#     print(a, b, args)
#     return sum(args)
#
#
# print(plus(2, 4, 5, 8, 78, 45, 12))



# def max1(iterable):
#     iterable = sorted(iterable)
#     return iterable[-1]
#
# print(max1([11, 4, 7, 9]))

# def len1(iterable):
#     counter = 0
#     for _ in iterable:
#         counter += 1
#     return counter
#
#
# print(len('123') + 7)
# print(len1('123') + 7)


# def show_objects(name, surname='unknown'):  # name - required positional argument
#     print('name:', name, 'surname:', surname) # surname - not required positional argument
#
#
# show_objects('peter', 'parker')  # peter - required positional argument
# show_objects(surname='lee', name='bruce')  # keyword argument


# print(help(len))
# print(len.__doc__)


# def max1(iterable):
#     max_value = 0
#     for i in iterable:
#         if i > max_value:
#             max_value = i
#     return max_value
#
#
# print(max1([3, 9, 76, 1, 4, 2, 6, 8]))


# def get_square(width: int, length: int) -> int:
#     """Принимает 2 числа (ширина, длина),
#      вщзвращает площадь прямоугольника."""
#     return width * length


# print(help(get_square))
# print(get_square.__doc__)



# n1 = int(input('width: '))
# n2 = int(input('length: '))
#
# square_2 = get_square(n1, n2)
# square_hall = get_square(12, 18)
#
# print(square_2, square_hall, sep='\n')

# width = 6
# length = 8
# square_2 = width * length
# print(square_2)
#
# width = 12
# length = 18
# square_hall = width * length
# print(square_hall)

def muiltiply(digit = int(input)):
    for i in digit:
        i *= digit
multiply()