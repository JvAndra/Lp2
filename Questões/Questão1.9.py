class Ball:
    def __init__(self, x, y, radius, xDelta, yDelta):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__xDelta = xDelta
        self.__yDelta = yDelta 

    def get_x(self):
        return self.__x
    
    def set_x(self,float):
         self.__x = float    

    def get_y(self):
        return self.__y
    
    def set_y(self,float):
         self.__y = float

    def get_radius(self):
        return self.__radius
    
    def set_radius(self,float):
         self.__radius = float
    
    def get_xDelta(self):
        return self.__xDelta
    
    def set_xDelta(self,float):
         self.__xDelta = float

    def get_yDelta(self):
        return self.__yDelta
    
    def set_yDelta(self,float):
         self.__yDelta = float

    def move(self):
        self.__x += self.__xDelta
        self.__y += self.__yDelta

    def reflectHorizontal(self):
        self.__xDelta = self.__xDelta * -1
        
    def reflectVertical(self):
        self.__yDelta = self.__yDelta * -1
    
    def __str__(self):
        return f"Ball [({self.__x},{self.__y}), velocidade = ({self.__xDelta},{self.__yDelta})]"

bola = Ball(1.1, 2.2, 10, 3.3, 4.4)
print(bola)
bola.set_x(80.0)
bola.set_y(35.0)
bola.set_radius(5)
bola.set_xDelta(4.0)
bola.set_yDelta(6.0)
print(bola)
print("x é:", bola.get_x())

print("y é:", bola.get_y())

print("radius é:", bola.get_radius())

print("xDelta é:", bola.get_xDelta())

print("yDelta é:", bola.get_yDelta())

xMin = 0.0
xMax = 100.0
yMin = 0.0
yMax = 50.0

for i in range(15):
    bola.move()
    print(bola)
    xNew = bola.get_x()
    yNew = bola.get_y()
    radius = bola.get_radius()

    if (xNew + radius) > xMax or (xNew - radius) < xMin:
        bola.reflectHorizontal()
    
    if (yNew + radius) > yMax or (yNew - radius) < yMin:
        bola.reflectVertical()