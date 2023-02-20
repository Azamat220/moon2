class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        married = "Married" if self.is_married else "Not married"
        print(f"Name: {self.fullname}. Age: {self.age}. {married}.")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_marks(self):
        return round(sum(self.marks.values()) / len(self.marks), 1)


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def salary_is_added(self):
        bonus = 0
        if self.experience > 3:
            bonus = self.salary * 0.05 * self.experience
        return self.salary + bonus


teacher = Teacher("Azamat Kudzaev", 33, True, 5, 40000)
teacher.introduce_myself()
print(f"Salary: {teacher.salary_is_added()}")


def create_students():
    students = []
    student1 = Student("Soslan Burnatsev", 18, False, {"Math": 5, "Chemistry": 3, "Physics": 3})
    student2 = Student("Alan Makeev", 18, False, {"Math": 3, "Chemistry": 5, "Physics": 3})
    student3 = Student("Aslan Tuskaev", 18, False, {"Math": 5, "Chemistry": 3, "Physics": 3})
    students.append(student1)
    students.append(student2)
    students.append(student3)
    return students


students = create_students()
for students in students:
    students.introduce_myself()
    print(f'Marks: {students.marks}')
    print(f'Average marks: {students.average_marks()}')
