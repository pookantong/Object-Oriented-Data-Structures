class Parenthesis:
    def __init__(self):
        self.par = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        self.all_par = ['[','{','(',')','}',']']

    def valid_parenthesis(self, pars):
        stack = []
        for char in pars:
            if char in self.all_par:
                if char in self.par:
                    stack.append(char)
                elif stack == []:
                    return print(f'{input} close paren excess')
                elif self.par[stack.pop()] != char:
                    return print(f'{input} Unmatch open-close  ')
        if stack != []:
            return print(f'{input} open paren excess   {len(stack)} : ', *stack, sep='')
        return print(f'{input} MATCH')


input = input('Enter expresion : ')
par = Parenthesis()
par.valid_parenthesis(input)