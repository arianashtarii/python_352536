import re
class Student:
    def __init__(self,code,name,title,units,teacher):
        self.code=code
        self.name=name
        self.title=title
        self.units=units
        self.teacher=teacher
    def student_validation(self):
        return re.match(r"^[A-Z][a-z]\s{3,30}$",self.name)
    def student_validation_2(self):
        return re.match(r"^[A-Z][a-z]\s{3,30}$",self.title)
    def student_validation_3(self):
        return re.match(r"^[0-9]{3,10}$",self.units)
    def student_validation_4(self):
        return re.match(r"^[A-Z][a-z]\s{3,30}$",self.teacher)
    def student_validation_5(self):
        return re.match(r"^[0,9]\s{3,10}$",self.code)

    math = Student(1234,"","math",2,"Ahmad Ahmadi")
    physics = Student("","","","","")
    chemistry = Student("","","","","")
