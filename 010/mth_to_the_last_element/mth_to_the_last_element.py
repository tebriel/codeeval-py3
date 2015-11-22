#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    input_file_name = sys.argv[1]
    with open(input_file_name) as input_file:
        for line in input_file.readlines():
            stuff = line.strip().split(' ')
            index = int(stuff.pop())
            if index > len(stuff):
                continue
            print(stuff[-index])
