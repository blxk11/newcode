# class Student:
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks
        
#     def check_marks(self):
#         if self.marks >= 40:
#             print(self.name, ": Pass")
#         elif self.marks < 40:
#             print(self.name,":Fail")
# student1 = Student("john",46)
# student2 = Student("marthin",33)
# student3 = Student("rahul",89)
 
            
# students = [student1,student2,student3]

# for student in students:
#     student.check_marks()


class Student:
    school = "ABC school"
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
student1 = Student("john",21)
student2 = Student("mathew",22)

Student.school = "XYZ school"

print(student1.name,Student.school)
print(student2.name,Student.school)