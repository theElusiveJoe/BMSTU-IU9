def concats_num(raw_string):
    return len(get_list_of_subs(raw_string))

def get_list_of_subs(raw_string):
    """
    принимает регулярку r
    возвращает список подрегулярок [r1 ... rn]: 
    r1+r2+...+rn == r  
    """
    if len(raw_string) > 0 and raw_string[0] == '*':
        raise Exception(f'подрегулярка {raw_string} начинается со звездочки')

    substrs = []
    while raw_string:
        split_index = get_first_concat_index(raw_string)

        if split_index == -1:
            return substrs + [raw_string]

        substrs.append(raw_string[:split_index])
        raw_string = raw_string[split_index:]

    return [raw_string]


def get_first_concat_index(raw_string):
    outside_brackets = 0
    for i in range(len(raw_string)):
        if i == 0:
            continue

        left_char = raw_string[i-1]
        right_char = raw_string[i]
        # print('l-r', left_char, right_char, outside_brackets)

        if left_char == '(':
            outside_brackets += 1
        if left_char == ')':
            outside_brackets -= 1

        if outside_brackets == 0:
            if right_char.isalpha() or right_char == '(':
                # print('конкат!')
                return i
            if right_char == left_char == '*':
                raise Exception(
                    f'в подрегулярке {raw_string} обнаружено 2 звездочки подряд')

    return -1


if __name__ == '__main__':
    tests = [
        'abcdef',
        'abcdef*',
        'a*bcdef',
        '*abcdef',
        'abc*def',
        'a(bc)def',
        'ab(cd)*ef*',
        'ab**c',
        '',
        'a*'
    ]

    foo = get_list_of_subs

    for test in tests:
        print('#######')
        print(f'"{test}"')
        try:
            print(f'"{foo(test)}"')
        except Exception as e:
            print(e)
