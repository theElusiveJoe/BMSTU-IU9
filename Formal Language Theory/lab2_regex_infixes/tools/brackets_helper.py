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


def find_closing_parenthesis_index_plus_one(long_str):
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


def split_to_left_and_right(raw_string):
    """разделяет строку на две части:
    не_левая_скобка* + псп + что-то_еще -> (не_левая_скобка* + псп, что-то_еще)
    строка_без псп -> (строка_без_псп, '')
    """

    i = find_closing_parenthesis_index_plus_one(raw_string)
    if i == -1:
        return raw_string, ''
    return raw_string[:i], raw_string[i:]


def remove_till_first_character(text, ch):
    if ch not in text:
        return text
    i = text.index(ch)
    return text[i+1:]


def has_side_extra_brackets(raw_string):
    "True, если первый и последний символ - скобки, причем взаимосвязанные"
    closing_bracket_index = find_closing_parenthesis_index_plus_one(raw_string)
    return len(raw_string) > 0 and raw_string[0] == '(' and closing_bracket_index == len(raw_string)


def remove_side_extra_brackets(raw_string):
    "Отрежет лишние скобки по краям, если такие имеются"
    while has_side_extra_brackets(raw_string):
        raw_string = raw_string[1:-1]
    return raw_string


if __name__ == '__main__':
    tests = [
        '(abcd)',
        'abcd',
        '(ab)(cd)',
        '(ab)(cd)()',
        '()(ab)(cd)()',
        '(((abc)())dd)',
        'a*|(ab)'
    ]

    foo = has_side_extra_brackets

    for test in tests:
        print('#######')
        print(f'"{test}"')
        try:
            print(f'"{foo(test)}"')
        except Exception as e:
            print(e)
