class Employee:
    def __init__(self,fname,lname,sal):
        self.firstname= fname
        self.lastname= lname
        self.salary=sal
    def myfunc(self):
        print("My name is {} and My surname is {}".format (self.firstname, self.lastname))
class Person(Employee):
    def __init__(self,fname,lname,sal,year):
        super().__init__(fname,lname,sal)
        self.gradyear= year

p1= Person("Pratik", "Khandelwal", 50000, 2012)
print (p1.gradyear)
p1.myfunc()

<<<<<<< HEAD
print('567')
=======
print('HELLO')
print('HELLO_NEW')
>>>>>>> c369546749424b11e522efdd0f7947085b6b6b16
print('HELLO_NEW_DONE')