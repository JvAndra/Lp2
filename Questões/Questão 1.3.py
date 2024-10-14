class Retangulo:
    
    def __init__(self, length = 1.0, width = 1.0):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length
    
    def _set_length(self,float):
        self.__length = float

    def get_width(self):
        return self.__width
    
    def _set_width(self,float):
        self.__width = float

    def getarea(self):
        area = float(self.__length * self.__width)
        return area
    
    def getperimeter(self):
        perimeter = float((2 * self.__length) + (2 * self.__width))
        return perimeter
    
    def __str__(self):
        return f"Retângulo [comprimento = {self.__length}, largura = {self.__width}]"
    
    
r1 = Retangulo(1.2, 3.4)
print(r1)
r2 = Retangulo()
print(r2)

r1._set_length(5.6)
r1._set_width(7.8)
print(r1)
print("comprimento é:", r1.get_length())
print("largura é:", r1.get_width())

print("a área é:", r1.getarea())
print("o perímetro é:", round(r1.getperimeter(),2))