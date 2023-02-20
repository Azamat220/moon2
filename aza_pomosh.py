class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def salary_of_teacher(self):
        if Beka.experience > 3:
            Beka.experience = Beka.experience - 3
            super_salary = Beka.salary + (Beka.salary * Beka.experience * 0.05)
            print(super_salary)


Beka = Teacher('Beka', 32, 'married', 5, 10000)
print(f'My name is  {Beka.fullname}. I am {Beka.age} and I am {Beka.is_married}'
       f'I have {Beka.experience} years experience in teaching. Nice to meet you!')
Beka.salary_of_teacher()
