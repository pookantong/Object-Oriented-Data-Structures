class FunString:
    def __init__(self, string) -> None:
        self.string = string
    
    def size(self):
        return len(self.string)
    
    def changeSize(self):
        string = list(self.string)
        res = []
        for char in string:
            if char <= 'Z' and char >= 'A':
                res.append(chr(ord(char)+32))
            elif char <= 'z' and char >= 'a':
                res.append(chr(ord(char)-32))
        return ''.join(res)
    
    def reverse(self):
        string = list(self.string)
        for i in range(len(self.string)-2, -1, -1):
            string.append(string.pop(i))
        return ''.join(string)
    
    def deleteSame(self):
        string = list(self.string)
        res = []
        [res.append(x) for x in string if x not in res]
        return ''.join(res)
    
str1, str2 = input("Enter String and Number of Function : ").split()

res = FunString(str1)

if str2 == "1" : print(res.size())

elif str2 == "2": print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())