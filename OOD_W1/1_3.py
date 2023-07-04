print('*** Reading E-Book ***')
text, highlight_char = input('Text , Highlight : ').split(',')
for char in text:
    if char == highlight_char:
        print(f'[{char}]', end='')
    else:
        print(char, end='')