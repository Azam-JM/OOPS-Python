class Student: 
    def __init__(self, name) -> None:
        self.name = name
    
class Course:
    def __init__(self, title) -> None:
        self.title = title
        self.students = []

    def enroll_student(self, student) -> None:
        self.students.append(student)
    

student1 = Student("Maznah")
student2 = Student("Inara")

course = Course("Kinder Garden")
course.enroll_student(student1)
course.enroll_student(student2)

print(f"Students enrolled in the Course {course.title} are {[student.name for student in course.students]}")