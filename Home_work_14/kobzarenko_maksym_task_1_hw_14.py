class Student():
    list_student: list = []  # Make list in which stored object reference

    def __new__(cls, *args, **kwargs):
        obj = super(Student, cls).__new__(cls)
        cls.list_student.append(obj)
        return obj

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def amount_student(cls):
        '''Function to count the number of student'''
        if hasattr(Student, "list_student"):
            return len(cls.list_student)

    @staticmethod
    def notice():
        '''Information about cource'''
        return f'Course "Python Basic" ands 26.06.2022. \n Next cource "Python Pro" will start 29.06.2022'


maksim = Student('Maksim', 'Kobzarenko', 26)
aleksandr = Student("Aleksandr", "Kozachkov", 36)

if __name__ == "__main__":
    print(Student.amount_student())
    print(Student.list_student)
    print(maksim.notice())

# Надо закоментировать "print" из импортированного модуля для того что бы в этом модуле не отображалась лишняя информация =)
from Home_work_12.kobzarenko_maksym_task_4_hw_12 import Car

toyata = Car()

if __name__ == '__main__':
    print(toyata.object_local_atribut())
