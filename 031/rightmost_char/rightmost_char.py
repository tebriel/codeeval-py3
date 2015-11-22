#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as open_file:
        for line in open_file.readlines():
            [text, char] = line.split(',')
            char = char.strip()
            position = text[::-1].find(char)
            if position != -1:
                position = len(text) - position - 1
            print(position)
