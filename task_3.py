class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _middle_grade(self):
        self.mid_grade = sum(sum(self.grades.values(),[]))/len(sum(self.grades.values(),[]))
        return self.mid_grade

    def __str__(self):
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'f'Средняя оценка за домашние задания: {self._middle_grade()}\n'
        f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {",".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self.mid_grade < other.mid_grade
  
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _middle_grade(self):
        self.mid_grade = sum(sum(self.grades.values(),[]))/len(sum(self.grades.values(),[]))
        return self.mid_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._middle_grade()}'
        return res    
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self.mid_grade < other.mid_grade

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
           
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python','Git']
some_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 9.9)
some_reviewer.rate_hw(some_student, 'Python', 9.9)
some_reviewer.rate_hw(some_student, 'Python', 9.9)

print(some_reviewer)
print(some_lecturer)
print(some_student)
