class translator:
    def __init__(self) -> None:
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
    def deciToRoman(self, num):
        romanNum = ''
        while num > 0:
            for key, val in self.romanNum.items():
                if val <= num:
                    romanNum = romanNum + key
                    num -= val
                    break
        return ''.join(romanNum)
    def romanToDeci(self, romanNum):
        val = 0
        i = 0
        while i < len(romanNum):
            if i+1 < len(romanNum) and romanNum[i]+romanNum[i+1] in self.romanNum:
                val += self.romanNum[romanNum[i]+romanNum[i+1]]
                i+=2
            else:
                val += self.romanNum[romanNum[i]]
                i+=1
        return val
                


num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))