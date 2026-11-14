class Student:
    school = "ABC school"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
    def display(self):
        print(self.name,self.age,self.school)
        
    @classmethod
    def change_school(self, new_school):
        cls.school = new_school
        
student1 = Student("john",21)
student2 = Student("rahul",22)

Student.school = "XYZ school"

student1.display()
student2.display()