# class Student:
#     def __init__(self,name,age,course,marks):
#         self.name = name
#         self.age = age
#         self.course = course 
#         self.marks = marks
#     def display(self):
#         print("Name is ",self.name)
#         print("Age is ",self.age)
#         print("Course is ",self.course)
#         print("Mark is",self.marks)
        
#     def change_mark(self,new_mark):
#         self.marks = new_mark
        
# student1 = Student("john",21,'python',56)
# student2 = Student("sathya",22,"django",66)
# student3 = Student("rahul",23,'java',55)

# student1.change_mark(77)

# student1.display()
# student2.display()
# student3.display()


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def check_mark(self):
        if self.marks >= 40:
            print(self.name,": pass")
        else:
            print(self.name,": Fail")
            
student1 = Student("john",43)
student2 = Student("martha",22)

student1.check_mark()
student2.check_mark()