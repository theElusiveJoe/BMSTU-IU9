#!/usr/bin/env python3
import argparse
import sys
import os
import re

# синтаксис оригинального grep
# grep [опции] шаблон [имена файлов...]
# команда | grep [опции] шаблон


def setup_parser():
    # -e - регулярное выражение
    # -i - нечувствительность к регистру
    # -m - количество совпадений, после которого программа завершается
    # -n - вывод номера строки
    parser = argparse.ArgumentParser(description="arguments description")
    parser.add_argument('-e', action="store_true", help="use regexpr")
    parser.add_argument('-i', action="store_true", help="case not sensitive")
    parser.add_argument('-m', action="store", type=int,
                        default="-1", help="how many matches should we find")
    parser.add_argument('-n', action="store_true", help="print line number")

    parser.add_argument('pattern', type=str, help="what we will look for")
    parser.add_argument('files', metavar='FILES', nargs='*', default=[],
                        help='the files(s) to search')

    return parser


def grep_lines(lines, filename, pattern, regexpr, case_sens, count_matches, line_number):
    line_num = 0
    matches = 0
    if case_sens:
        pattern = pattern.lower()
        lines = lines.lower()

    lines = lines.splitlines()
    if regexpr:
        for line in lines:
            line_num += 1
            if count_matches and matches == count_matches:
                break
            if re.search(pattern, line):
                if not filename == "":
                    print(filename, ":", end='', sep='')
                matches += 1
                if line_number:
                    print(line_num, ":", end='', sep='')
                print(line)
    else:
        for line in lines:
            line_num += 1
            if count_matches and matches == count_matches:
                break
            if pattern in line:
                if not filename == "":
                    print(filename, ":", end='', sep='')
                matches += 1
                if line_number:
                    print(line_num, ":", end='', sep='')
                print(line)


def grep_many_sources(paths, pattern, regexpr, case_sens, count_matches, line_number):
    if not paths:
        strings = sys.stdin
        grep_lines(strings.read(), '', pattern, regexpr, case_sens, count_matches, line_number)
    elif len(paths) == 1:
        if os.path.isfile(paths[0]):
            if os.access(paths[0], os.R_OK):
                file = open(paths[0])
                grep_lines(file.read(), '', pattern, regexpr, case_sens, count_matches, line_number)
            else:
                print(paths[0], ": Permission denied ", sep='')
        else:
            print(paths[0], ": no such file or directory ", sep='')
    else:  # это разделение нужно, чтобы для ениного файла не выводилось его название
        for path in paths:
            if os.path.isfile(path):
                if os.access(path, os.R_OK):
                    file = open(path)
                    grep_lines(file.read(), path, pattern, regexpr, case_sens, count_matches, line_number)
                else:
                    print(path, ": Permission denied ", sep='')
            else:
                print(path, ": no such file or directory ", sep='')


def main():
    parser = setup_parser()
    args = parser.parse_args()

    grep_many_sources(args.files, args.pattern, args.e, args.i, args.m, args.n)


if __name__ == '__main__':
    main()
