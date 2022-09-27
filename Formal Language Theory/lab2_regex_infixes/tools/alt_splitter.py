def substrs_num(raw_string):
    if get_first_alt_sign_index(raw_string) == -1:
        return 1
    return len(get_split_indexes(raw_string)) + 1


def get_split_indexes(raw_string):
    outside_brackets = 0
    alt_sign_indexes = []
    for i, cur_char in enumerate(raw_string):
        if cur_char == '|' and outside_brackets == 0:
            alt_sign_indexes.append(i)
        elif cur_char == '(':
            outside_brackets += 1
        elif cur_char == ')':
            outside_brackets -= 1
    return alt_sign_indexes


def get_list_of_subs(raw_string):
    """
    принимает регулярку r
    возвращает список подрегулярок [r1 ... rn]: 
    r1 | r2 | ... | rn  == r  
    """

    # if substrs_num(raw_string) == 1:
    #     return [raw_string]

    substrs = []
    while raw_string:
        split_index = get_first_alt_sign_index(raw_string)

        if split_index == -1:
            return substrs + [raw_string]

        substrs.append(raw_string[:split_index])
        raw_string = raw_string[split_index+1:]

    return substrs + ['']


def get_first_alt_sign_index(raw_string):
    outside_brackets = 0
    for i, cur_char in enumerate(raw_string):
        if cur_char == '|' and outside_brackets == 0:
            return i
        elif cur_char == '(':
            outside_brackets += 1
        elif cur_char == ')':
            outside_brackets -= 1
    return -1


if __name__ =='__main__':
    tests = [
    'abc',
    '|abc',
    'abc|',
    'a|b|c',
    '|a|b|c',
    '(ab)|cd',
    '(a||b)|cd|',
    'c|a',
    'a*|(ab)'
    ]

    for test in tests:
        print('#######')
        print(test)
        print(get_list_of_subs(test))