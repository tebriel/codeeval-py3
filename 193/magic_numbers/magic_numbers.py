#!/usr/bin/env python3
import sys


def should_skip(number_str):
    # Skip numbers with a 0 in them or duplicate digits
    return '0' in number_str or len(set(number_str)) < len(number_str)


def process_line(line):
    [start, end] = line.strip().split(' ')
    start = int(start)
    end = int(end)

    results = []
    for num in range(start, end+1):
        repeats = False
        num_str = unvisited_nums = str(num)
        digit = int(num_str[0])

        if should_skip(num_str):
            continue

        while len(unvisited_nums) > 0:
            digit_str = str(digit)
            unvisited_nums = unvisited_nums.replace(digit_str, '')
            idx = num_str.index(digit_str)
            next_num = num_str[(digit + idx) % len(num_str)]

            # Last number and it points back at the beginning
            if len(unvisited_nums) == 0 and next_num == num_str[0]:
                break

            if next_num == digit_str:
                repeats = True
                break
            elif next_num not in unvisited_nums:
                repeats = True
                break

            digit = int(next_num)

        if not repeats:
            results.append(num_str)

    return results


if __name__ == '__main__':
    input_file_name = sys.argv[1]
    with open(input_file_name) as input_file:
        lines = input_file.readlines()

    for line in lines:
        results = process_line(line)
        if results:
            print(' '.join(results))
        else:
            print(-1)
