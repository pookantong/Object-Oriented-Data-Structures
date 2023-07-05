class MyInt :
    def __init__(self, num) -> None:
        self.val = num
        self.romanNum = {
            "M" : 1000,
            "CM" : 900,
            "D" : 500,
            "CD" : 400,
            "C" : 100,
            "XC" : 90,
            "L" : 50,
            "XL" : 40,
            "X" : 10,
            "IX" : 9,
            "V" : 5,
            "IV" : 4,
            "I" : 1
        }
    
    def __add__(self, val2):
        return MyInt(int((self.val + val2.val)*1.5))
    
    def toRoman(self):
        valTemp = self.val
        romanNum = ''
        while valTemp > 0:
            for key, val in self.romanNum.items():
                if val <= valTemp:
                    romanNum = romanNum + key
                    valTemp -= val
                    break
        return romanNum
                
            
print(' *** class MyInt ***')
num1, num2 = [int(x) for x in input('Enter 2 number : ').split()]
a = MyInt(num1)
b = MyInt(num2)
print(f'{a.val} convert to Roman : {a.toRoman()}')
print(f'{b.val} convert to Roman : {b.toRoman()}')
print(f'{a.val} + {b.val} = {(a+b).val}')