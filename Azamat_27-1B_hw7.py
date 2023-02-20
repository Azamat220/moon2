  #1
ten = list(range(1, 11))
print(f'Список чисел от 1 до 10: {ten}')

 # 2
evens = list(filter(lambda i: 1 % 2 == 0,ten))
print(f'Чётные числа из списка: {evens}")

 # 3
square = list (map (lambda i: i**2, evens))
print (f'Квадрат чётных чисел: {square}')

 # 4
def index(lst=ten):
    while True:
        try:

            ind = int(input ( 'Введите индекс или 00 для выхода: "))

            if ind == 00:
                break
                print (ten [ind])
        except IndexError:
            print (f'Введите индекс до{len (lst)-1}')
        except ValueError:
            print( 'Вводить нужно только числа!')
index()