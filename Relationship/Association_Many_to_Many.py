"""
Uses-a relationship
"""

class Students:
    def __init__(self, name) -> None:
        self.name = name
        self.courses = []

    def enroll_courses(self, course) -> None:
        self.courses.append(course)
        course.students.append(self)

class Courses:
    def __init__(self, title) -> None:
        self.title = title
        self.students = []

student1 = Students("Maxnah")
student2 = Students("Inaxa")
course1  = Courses("Maths")
course2 = Courses("Chemistry")

student1.enroll_courses(course1)
student1.enroll_courses(course2)

student2.enroll_courses(course2)

print(f"Students registered Course1: {course1.title} : {[student.name for student in course1.students]}")
print(f"Students registered Course2: {course2.title} : {[student.name for student in course2.students]}")
print(f"Courses registered by Student1: {student1.name} : {[student.title for student in student1.courses]}")
print(f"Courses registered by Student2: {student2.name} : {[student.title for student in student2.courses]}")