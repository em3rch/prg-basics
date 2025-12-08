# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.rok = 0


def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.rok = 1
    student2.name = "Olivia"
    student2.age = 21
    student2.rok = 2

    student3.name = "Artem"
    student3.age = 18 
    student3.rok = 1

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old and studies on {student1.rok} year.')
    print(f'{student2.name}, {student2.age} years old and studies on {student2.rok} year.')
    print(f'{student3.name}, {student3.age} years old and studies on {student3.rok} year.')


if __name__ == "__main__":
    main()