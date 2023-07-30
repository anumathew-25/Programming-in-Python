from abc import ABC,abstractmethod
class Shape(ABC):
    def area(self):
        pass
    def circumference(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def  circumference(self):
        return 2*3.14*self.radius
    
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def  circumference(self):
        return 2*(self.length+self.breadth)
c=Circle(5)  
r=Rectangle(2,3)
print(c.area())
print(c.circumference())
print(r.area())
print(r.circumference())

