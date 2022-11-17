class Class:
    __students_count = 22

    def __init__(self, name):
        name = name
        students = []
        grades = []

    def add_student(self, name: str, grade: float):
        if len(students) < Class.__students_count:
            students.append(name)
            grades.append(grade)

    def get_average_grade(self):
        return round(sum(grades) / len(grades), 2)

    def __repr__(self):
        students = ", ".join(students)
        return f'The students in {name}: {students}. Average grade: {get_average_grade()}'

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
