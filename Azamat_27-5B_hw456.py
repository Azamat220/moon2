
proga = {
    'courses': ['iOS', 'Основы программирования', 'UX/UI']
}
GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
GeekTech.update(proga)
GeekTech['courses'] = set(['Android', 'Backend', 'Frontend','iOS','Основы программирования', 'UX/UI'])
long = len(GeekTech['courses'])
del GeekTech['bag']
GeekTech['address'] = 'Ибраимова 103'
GeekTech['inst_akk'] = 'geektech_edu'
GeekTech['phone_number'] = '0507052018'
for k, v in GeekTech.items():
    print(f'{k} >> {v}')
print(f'Дата основания:2018\n{GeekTech}\n Количество курсов: {long}')



