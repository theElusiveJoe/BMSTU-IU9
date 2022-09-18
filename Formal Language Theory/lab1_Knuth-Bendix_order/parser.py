import re

from term import Term
from rule import Rule

test_structure = r"(?P<order_param>\banti-lexicographic\b|\blexicographic\b)\s*constructors\s*=\s*(?P<constructors>(?:\w|,|\(|\))*)\s*variables\s*=\s*(?P<variables>(?:(\w|\s|,)*))\s*(?P<terms>.*)"


class Parser():
    def parse_file(self, file_name):
        with open(file_name, 'r') as f:
            text = f.read().strip()

        text = re.sub('\s+', ' ', text)
        match = re.match(test_structure, text)

        self.order_param = match.group('order_param')
        # print("➡ self.order_param :", self.order_param)

        self.variables = match.group('variables').replace(' ', '').split(',')
        # print("➡ self.variables :", self.variables)

        self.constructors = dict()
        self.constructors.update([
            (c[0], int(re.findall('\d+', c)[0]))
            for c in match.group('constructors').replace(' ', '').split(',')
        ])
        # print("➡ self.constructors :", self.constructors)
        
        rules = split_to_pathernesses(match.group('terms'))
        # print("➡ rules :", rules)
        self.rules = []
        for rule in rules:
            parsed_rule = self.parse_rule(rule)
            # print('PARSED RULE', parsed_rule)
            self.rules.append(parsed_rule)


    def parse_rule(self, pair_string):
        left, right = list(map(lambda x: self.parse_term(x.strip()), pair_string[1:-1].split('::=')))
        return Rule(left, right)

    def parse_term(self, term_string: str):
        """Принимает на вход строку терма, не обрамленного скобочками"""
        term_string = term_string.strip()

        # print('PARSE_TERM', term_string, end=' - ')
        # если терм лежит в множестве переменных
        if term_string in self.variables:
            # print('    это переменная')
            return Term(term_type='var', name=term_string)

        # если терм - число
        if re.match('\d+', term_string) is not None:
            # print('это число')
            return Term(term_type='const', content=term_string)

        # получается, терм - конструктор
        # print('это конструктор')
        return Term(term_type='constructor', name=term_string[0], content=self.parse_subterms(term_string))

    def parse_subterms(self, term_string):
        all_subterms_str = re.match(r'\w\((?P<subterms>.*)\)',
                                    term_string).group('subterms').strip()
        
        subterms = []
        # print("начинаю парсить аргументы:'", all_subterms_str, "'")
        for _ in range(self.constructors[term_string[0]]) :

            # print(f'осталось распарсить аргументы: "{all_subterms_str}"')

            if all_subterms_str[0] in self.variables:
                # print(f'найдена переменная "{all_subterms_str[0]}"')
                subterms.append(self.parse_term(all_subterms_str[0]))
                all_subterms_str = remove_till_first_character(all_subterms_str, ',').strip()
                continue

            match = re.match(r'(?P<number>\d+).*', all_subterms_str)
            if match:
                # print(f'найдена константа "{match.group("number")}"')
                subterms.append(self.parse_term(match.group('number')))
                all_subterms_str = remove_till_first_character(all_subterms_str, ',').strip()
                continue
                
            i = find_closing_parenthesis(all_subterms_str)
            # print(f'найден конструктор"{all_subterms_str[:i]}"')
            # print('i =', i)
            subterms.append(self.parse_term(all_subterms_str[:i]))
            all_subterms_str = remove_till_first_character(all_subterms_str[i:], ',').strip()
            
            

        return subterms


def split_to_pathernesses(whole_string):
    """Принимает строку. Возвращает список подстрок
    - содержимое скобочек нулевого уровня + сами скобочки"""
    counter = 0
    starts = []
    for i, ch in enumerate(whole_string):
        if ch == '(':
            counter += 1
            if counter == 1:
                starts.append(i)
        elif ch == ')':
            counter -= 1
    starts.append(len(whole_string))
    return [whole_string[starts[i]:starts[i+1]].strip() for i in range(len(starts)-1)]


def find_closing_parenthesis(long_str):
    """Находит закрывающую скобку 0 уровня,
    возвращает индекс следующего за ней символа
    Если не находит, возвращает -1"""
    counter = 0
    left_p = 0
    for i, x in enumerate(long_str):
        if x == '(':
            counter += 1
        elif x == ')':
            counter -= 1
            if counter == 0:
                return i+1

    return -1


def remove_till_first_character(text, ch):
    if ch not in text:
        return text
    i = text.index(ch)
    return text[i+1:]


