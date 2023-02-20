# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married
#
#     def introduce_myself(self, hobby):
#         print(f'My name is {self.fullname}  I am programmer in the New-York City \n'
#               f"I am {self.age}  and now {self.is_married}. I have a hobby . It's {hobby} ")
#
#
# man = Person('Adil', 16, 'single')
# print(f'Fullname: {man.fullname} Age: {man.age} Married: {man.is_married}')
#
# man.introduce_myself('Soccer')
#
#
# class Student(Person):
#     def __init__(self, fullname, age, is_married, marks):
#         super().__init__(fullname, age, is_married)
#         self.marks = marks
#     def gpa (self):
#         grades = 0
#         for i in marks.values():
#             grades += i
#         print(f"Student's  GPA: {round((grades / marks_amount), 1)}")
#
# marks = {'math': 85,
#          'biology': 60,
#          'PE': 78}
#
# marks_amount = len(marks.values())
#
# Student.gpa('middle grade')
#
# class Teacher(Person):
#     salary = 10000
#     def __init__(self, fullname, age, is_married, experience):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience
#
#     def salary_of_teacher(self, zp):
#         if Beka.experience > 3:
#             while(Beka.experience <= 0):
#
#                 Beka.salary + Beka.salary * 0.05
#         return super_salary
#
#
# Beka = Teacher('Beka', 32, 'married', 5)
# print(f'My name is  {Beka.fullname}. I am {Beka.age} and I am {Beka.is_married}'
#        f'I have {Beka.experience} years experience in teaching. Nice to meet you!')
# Beka.salary_of_teacher('pribavka')

# class Teacher(Person):
#     def __init__(self, fullname, age, is_married, experience, salary):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience
#         self.salary = salary
#
#     def salary_of_teacher(self):
#         if Beka.experience > 3:
#             Beka.experience = Beka.experience - 3
#             super_salary = Beka.salary + (Beka.salary * Beka.experience * 0.05)
#             print(super_salary)
#
#
# Beka = Teacher('Beka', 32, 'married', 5, 10000)
# print(f'My name is  {Beka.fullname}. I am {Beka.age} and I am {Beka.is_married}'
#        f'I have {Beka.experience} years experience in teaching. Nice to meet you!')
# Beka.salary_of_teacher()
#
# def create_students(a,b,c):
#     student_1 = Student('Azake', 17, 'single', )
#     student_2 = Student('Aldyar', 16, 'single', )
#     student_3 = Student('Avenir', 18, 'single', )
#









# class Figure:
#     unit = 'cm'
#
#     def __init__(self):
#         pass
#
#     def calculate_area(self):
#         pass
#
#     def info(self):
#         pass
#
#
# class Circle(Figure):
#     def __init__(self, radius):
#         super().__init__()
#         self.__radius = radius
#
#     def get_radius(self):
#         return self.__radius
#
#     def set_radius(self, value):
#         if isinstance(value, int) and value > 0:
#             self.__radius = value
#         else:
#             print('Wrong value for radius , it must be a positive number')
#
#     def calculate_area(self):
#         radius_2 = self.__radius * self.__radius
#         return radius_2 * 3.14
#
#     def info(self):
#         return (f'Circle radius: {self.__radius}{Figure.unit}, '
#                 f'area: {i.calculate_area()}{Figure.unit}')
#
#
# class RightTriangle(Figure):
#     def __init__(self, side_a, side_b):
#         super().__init__()
#         self.__side_a = side_a
#         self.__side_b = side_b
#
#     def get_side_a(self):
#         return self.__side_a
#
#     def set_side_a(self, value):
#         if isinstance(value, int) and value > 0:
#             self.__side_a = value
#         else:
#             print('Wrong value for side A , it must be a positive number')
#
#     def get_side_b(self):
#         return self.__side_b
#
#     def set_side_b(self, value):
#         if isinstance(value, int) and value > 0:
#             self.__side_b = value
#         else:
#             print('Wrong value for side B , it must be a positive number')
#
#     def calculate_area(self):
#         triangle = 0.5 * self.__side_a * self.__side_b
#         return triangle
#
#     def info(self):
#         return(f'RightTriangle side a: {self.__side_a}{Figure.unit}, side b: {self.__side_b}{Figure.unit}, '
#                f'area: {i.calculate_area()}{Figure.unit}.')
#
#
# circle_1 = Circle(10)
# circle_2 = Circle(5)
# triangle_1 = RightTriangle(4, 5)
# triangle_2 = RightTriangle(5, 6)
# triangle_3 = RightTriangle(5, 8)
#
#
# list_of_figures = [circle_1, circle_2, triangle_1, triangle_2, triangle_3]
# for i in list_of_figures:
#     print(i.info())
