#!/usr/bin/env python3
import argparse
import sys
import os
import re


# синтаксис оригинального wc
# grep [опции] шаблон [имена файлов...]
# команда | grep [опции] шаблон
# -c, -m, -w, -l


def setup_parser():
    # -l - строки
    # -w - слова
    # -m - показывать количество символов
    # -с - размер объекта в байтах
    parser = argparse.ArgumentParser(description="arguments description")
    parser.add_argument('-l', action="store_true", help="count lines")
    parser.add_argument('-w', action="store_true", help="count words")
    parser.add_argument('-m', action="store_true", help="count symbols")
    parser.add_argument('-c', action="store_true", help="size in bytes")

    parser.add_argument('files', metavar='FILES', nargs='*', default=[],
                        help='the files(s) to search in')

    return parser


def count_in_text(text, symbols, words, lines):
    s = len(text)
    w = len(text.split())
    l = len(text.splitlines())
    if lines:
        print(l, end='    ')
    if words:
        print(w, end='    ')
    if symbols:
        print(s, end='    ')
    return [s, w, l]


def wc_many_sources(paths, bbytes, symbols, words, lines):
    if not paths:
        textfile = sys.stdin
        text = textfile.read()
        if bbytes:
            print(sys.getsizeof(text), end="    ")
        count_in_text(text, symbols, words, lines)
        print()
    elif len(paths) == 1:
        if os.path.isfile(paths[0]):
            if os.access(paths[0], os.R_OK):
                if bbytes:
                    print(os.path.getsize(paths[0]), end='    ')
                file = open(paths[0])
                count_in_text(file.read(), symbols, words, lines)
                print(paths[0])
            else:
                print(paths[0], ": Permission denied ", sep='')
        else:
            print(paths[0], ": no such file or directory ", sep='')
    else:  # это разделение нужно, чтобы для единого файла не выводилось total
        tc = tw = tl = ts = 0
        for path in paths:
            if os.path.isfile(path):
                if os.access(path, os.R_OK):
                    if bbytes:
                        tmp = os.path.getsize(path)
                        tc += tmp
                        print(tmp, end='    ')
                    file = open(path)
                    single = count_in_text(file.read(), symbols, words, lines)
                    ts += single[0]
                    tw += single[1]
                    tl += single[2]
                    print(path)
                else:
                    print(path, ": Permission denied ", sep='')
            else:
                print(path, ": no such file or directory ", sep='')
        if lines:
            print(tl, end='    ')
        if words:
            print(tw, end='    ')
        if symbols:
            print(ts, end='    ')
        if bbytes:
            print(tc, end='    ')
        print("total")


def main():
    parser = setup_parser()
    args = parser.parse_args()
    if not (args.l or args.w or args.m or args.c):
        args.l = args.w = args.m = True

    wc_many_sources(args.files, args.c, args.m, args.w, args.l)


if __name__ == '__main__':
    main()
