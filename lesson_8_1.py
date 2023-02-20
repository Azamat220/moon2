"""Работа с файлами."""
# w - write (перезапись)
# a - add (дозапись)
# x - бесконфликтный режим записи
# r - чтение

znacheiya = {}
from random import choice

with open('students.txt', 'r', encoding='UTF-8') as students:
    students_list = students.readlines()
    students_list = [i.rstrip() for i in students_list]
    with open('materials.txt', encoding='UTF-8') as materials:
        materials_list = materials.readlines()
        materials_list = [i.rstrip() for i in materials_list]
        with open('results.txt', 'a', encoding='UTF-8'\) as results:
            while len(students_list) > 0:
                print("осталось студентов", len(students_list))
                chosen_student = choice(students_list)
                chosen_material = choice(materials_list)
                rate = int(input(
                    f"{chosen_student}\n"
                    f"тема: {chosen_material}:\n"
                    f"оценка: "))
                results.write(
                    f"имя: {chosen_student} тема: {chosen_material[:1]} "
                    f"оценка: {rate}\n")
                students_list.remove(chosen_student)

znacheniya









