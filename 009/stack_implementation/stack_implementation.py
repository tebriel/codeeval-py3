#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as input_file:
        for line in input_file.readlines():
            print(' '.join(line.strip().split(' ')[::-2]))
