pi = 3.141592653589793238462643383279502884197169399375105820974
class Spherical:
    def __init__(self, radius) -> None:
        self.radius = radius
    def changeR(self, radius):
        self.radius = radius
    def findVolume(self):
        return 4/3*pi*pow(self.radius, 3)
    def findArea(self):
        return 4*pi*pow(self.radius, 2)
    def __str__(self):
        return f'Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()}'

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)