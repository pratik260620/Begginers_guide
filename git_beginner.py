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

print('hello')
<<<<<<< HEAD
print('HIII')



=======
print('hello world')
print('hey')
Print('Changes done in this file)
print('123456')
>>>>>>> e9d31398bb256e3ba558e0639c9c6a0307807028
