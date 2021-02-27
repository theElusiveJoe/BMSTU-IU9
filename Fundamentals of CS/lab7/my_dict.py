#!/usr/bin/env python3
import os
import sys

def parsedict(file_name):
    if os.path.isfile(file_name):
        if os.access(file_name, os.R_OK):
            file = open(file_name)
            text = file.read()
            new_text = ""
            for symbol in text:
                if symbol.isalpha() or symbol == "'" or symbol.isspace():
                    new_text += symbol
            return new_text.lower().split()
        else:
            print(dict_file, ": Permission denied ", sep='')
            sys.exit()
    else:
        print(dict_file, ": no such file or directory ", sep='')
        sys.exit()

def parsewords(file_name):
    if os.path.isfile(file_name):
        if os.access(file_name, os.R_OK):
            file = open(file_name)
            lines = file.read().splitlines()
            words = []
            for i in range(0, len(lines)-1):
                word=""
                k=0
                for j in range(0, len(lines[i])-1):
                    if lines[i][j].isalpha() or lines[i][j] == "'":
                        if word == "":
                            k = j
                        word += lines[i][j]
                    elif not word == '':
                        words.append([word, k+1, i+1])
                        word = ""
            for word in words:
                word[0] = word[0].lower()
            return words
        else:
            print(dict_file, ": Permission denied ", sep='')
            sys.exit()
    else:
        print(dict_file, ": no such file or directory ", sep='')
        sys.exit()


def main():
    if len(sys.argv) < 3:
        print("not enough arguments")
        sys.exit()

    dict_file = sys.argv[1]
    text_file = sys.argv[2]
    dict = parsedict(dict_file)
    words = parsewords(text_file)
    for word in words:
        if not word[0] in dict:
            print(word[2], ",  ", word[1], ",  ", word[0], sep='')

if __name__ == '__main__':
    main()
