sogl = 'qwrtpsdfghjklzxcvbnmйцукнгшщзхфвпрлджчсмтбQWRTPSDFGHJKLZXCVBNMЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ'
glas = 'yuoaiаиеоуыэюяeёЁУЕЫАОЭЯИЮYEUIOA'
while True:
    word = input('Слово: ')
    azake = len(word)
    if word == 'exit' or word == 'выход':
        break
    a = 0
    b = 0
    for i in word:
        if i in sogl:
            b += 1
        elif i in glas:
            a += 1
        x = a / azake * 100
        y = b / azake * 100
    print(f'Количество букв: {len(word)} \nСогласных: {b} \nГласных: {a}\nГласные/Согласные: {round(x,2)}%/{round(y,2)}%')