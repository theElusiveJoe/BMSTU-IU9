from models.regex_comparator import Is_in_checker
from models.regex_parser import Regex_parser


def test_isinchecker(raw1, raw2):
    r1 = Regex_parser(raw_text=raw1).parse().simplify()
    r2 = Regex_parser(raw_text=raw2).parse().simplify()

    ch = Is_in_checker()
    res = ch.l1_in_l2(r1, r2)
    print(res)
    return res


if __name__ == '__main__':
    with open('tests/isinchecker_tests.txt', 'r') as file:
        lines = file.read().split('\n')
        # lines.sort(key=len)
        tests = list([l.split()for l in filter(lambda x: len(x) > 0, lines)])
        for test in tests:
            try:
                assert bool(int(test[2])) == test_isinchecker(test[0], test[1])
            except AssertionError as e:
                print(bool(int(test[2])), test_isinchecker(test[0], test[1]))

    # raw1 = 'a'
    # raw2 = 'aaa'
    # test_isinchecker(raw1, raw2)
