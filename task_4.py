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
        f'Фамилия: {self.surname}\n'
        f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {",".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self._middle_grade() < other._middle_grade()
  
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
        res = (f'Имя лектора: {self.name}\n'
        f'Фамилия лектора: {self.surname}\n')
        return res    
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self._middle_grade() < other._middle_grade()

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
        res = (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n')
        return res      

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

new_lecturer = Lecturer('Good', 'Buddy')
new_lecturer.courses_attached += ['Git']

old_lecturer = Lecturer('Old', 'Man')
old_lecturer.courses_attached += ['Java']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python','Git', 'Java']
some_student.finished_courses += ['Введение в программирование']
some_student.rate_lecturer(some_lecturer, 'Python', 3)
some_student.rate_lecturer(new_lecturer,'Git', 9)
some_student.rate_lecturer(old_lecturer,'Java', 7)

new_student = Student('Every', 'Day', 'your_gender')
new_student.courses_in_progress += ['Python','Git','Java']
new_student.finished_courses += ['Введение в программирование']
new_student.rate_lecturer(some_lecturer, 'Python', 7.5)
new_student.rate_lecturer(new_lecturer,'Git', 6)
new_student.rate_lecturer(old_lecturer,'Java', 9)

some_reviewer = Reviewer('Every', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 9.1)
some_reviewer.rate_hw(new_student, 'Python', 5)

easy_reviewer = Reviewer('Just', 'Cause')
easy_reviewer.courses_attached += ['Git', 'Java']
easy_reviewer.rate_hw(some_student, 'Git', 9)
easy_reviewer.rate_hw(some_student, 'Java', 3)
easy_reviewer.rate_hw(new_student, 'Git', 8)
easy_reviewer.rate_hw(new_student, 'Java', 7.6)

students = [some_student, new_student]
marks_python = []
marks_git = []
marks_java = []
for student in students:
    for subject, mark in student.grades.items():
        if subject == "Python":
            marks_python.append(mark)
        elif subject == "Git":
            marks_git.append(mark)
        elif subject == "Java":
            marks_java.append(mark)
mid_python = sum(sum(marks_python,[]))/len(sum(marks_python,[]))   
mid_git = sum(sum(marks_git,[]))/len(sum(marks_git,[]))
mid_java = sum(sum(marks_java,[]))/len(sum(marks_java,[]))

lecturers = [new_lecturer, some_lecturer, old_lecturer]
comment_python = []
comment_git = []
comment_java = []
for lecturer in lecturers:
    for subject, mark in lecturer.grades.items():
        if subject == "Python":
            comment_python.append(mark)
        elif subject == "Git":
            comment_git.append(mark)
        elif subject == "Java":
            comment_java.append(mark)
teach_python = sum(sum(comment_python,[]))/len(sum(comment_python,[]))   
teach_git = sum(sum(comment_git,[]))/len(sum(comment_git,[]))
teach_java = sum(sum(comment_java,[]))/len(sum(comment_java,[]))

print(some_lecturer,f'Средняя оценка за лекции по предмету: {teach_python}\n{some_lecturer.__lt__(new_lecturer)}\n')
print(new_lecturer,f'Средняя оценка за лекции по предмету: {teach_git}\n{new_lecturer.__lt__(old_lecturer)}\n')
print(old_lecturer,f'Средняя оценка за лекции по предмету: {teach_java}\n{old_lecturer.__lt__(some_lecturer)}\n')

print(some_student)
print(new_student)
print(f'Средняя оценка за курс Python: {mid_python}\nGit: {mid_git}\nJava: {mid_java}\n')

print(some_reviewer)
print(easy_reviewer)
