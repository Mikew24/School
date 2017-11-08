import math
class shape():
    def __init__(self,radius):
        self.radius=radius
    def __init__(self,length=0,width=0,radius=0):
        self.length=length
        self.width=width
        self.radius=radius
    def getArea(self):
        return self.legth*self.width
class rectangle(shape):
    def __init__(self,length,width):
        shape.__init__(self,length,width)
    def getArea(self):
       return  self.length*self.width
    def getPermeter(self):
        return 2*self.length+2*self.width
class circle(shape):
    def __init_ (self,radius):
        shape.__init__(self,0,0,radius)
    def getArea(self):
        return math.pi*self.radius*self.radius
    def getPerimeter(self):
        return 2*math.pi*self.radius
spice= rectangle(5,4)
print(spice.getArea())
print(spice.getPermeter())
spicey= circle(0,0,6)
print(spicey.getArea())
print(spicey.getPerimeter())
K=[spice,spice]
for elem in K:
   print( elem.getArea())
   print(elem.getPermeter())
