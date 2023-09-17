import re

"""
Идентификаторы: последовательности буквенных символов Unicode и цифр, начинающиеся с буквы.
Числовые литералы: 
    десятичные литералы представляют собой последовательности десятичных цифр, 
    шестнадцатиричные — начинаются на десятичную цифру, содержат шестнадцатеричные цифры (в любом регистре) и заканчиваются символом «h». 
Ключевые слова «mov», «eax».
"""


class Parser:
    def __init__(self, file_name):
        self.lines = open(file_name, 'r').readlines()
    
    def skip_spaces(self):
        new_line = self.line.lstrip()
        self.i += len(self.line) - len(new_line)
        self.line = new_line

    def skip(self, s):
        self.i += len(s)
        self.line = self.line[len(s):]

    def parse(self):
        errors = list()
        lexems = list()
        
        variants = (
            ('IDENTIFIER', r'^([^\W\d_][^\W_]*)',),
            ('KEYWORD', r'^(mov|eax)'),
            ('HEXIMAL', r'^(\d[A-Fa-f\d]*h)'),
            ('DECIMAL', r'^(\d+)'),
        )

        for linenum, line in enumerate(self.lines):
            self.line = line.rstrip()
            self.i = 1
            linenum += 1
            while self.line:
                if self.line[0].isspace():
                    self.skip_spaces()
                    continue

                for typ, pattern in variants:
                    match = re.findall(pattern, self.line)
                    if match:
                        result = match[0]
                        lexems.append(
                            (typ, (linenum, self.i), result.strip())
                        )
                        self.skip(result)

                        print((typ, (linenum, self.i), result.strip()))
                        break
                else:
                    print('error', (linenum, self.i), self.line)
                    errors.append(
                        (linenum, self.i)
                    )
                    self.skip(' ')
                
        return lexems, errors


if __name__ == '__main__':
    lexems, errors = Parser('test.txt').parse()

    print('------')

    for x in lexems:
        print(x)

    print('------')

    for x in errors:
        print('syntax error', x)