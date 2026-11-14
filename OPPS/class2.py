# class Student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def introduce(self):
#         print("name is ",self.name)
#         print("age is ", self.age)
#         print("course is ",self.course)
        
# student1 = Student("John",21,'python')
# student2 = Student("rahul",22,"django")
# student3 = Student("sathya",23,"jave")

# student1.introduce()
# student2.introduce()
# student3.introduce()


class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age 
        self.course = course
    def display(self):
        print("My name is ",self.name)
        print("My course is",self.course)
        print("My age is ",self.age)
    def change(self,new_course):
        self.course = new_course
    def change_age(self,new_age):
        self.age = new_age
        
student1 = Student("john",21,"python")
student2 = Student("sathya",22,"django")
student3 = Student("rahul",23,'java')

student1.display()
student2.display()
student3.display()
student2.change("react")
student2.display()