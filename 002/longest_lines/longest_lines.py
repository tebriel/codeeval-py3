#!/usr/bin/env python3
import sys
from collections import defaultdict


class LongestLines(object):
    def __init__(self, input_file):
        self.input_file = input_file
        self.lengths = defaultdict(list)
        self.desired_count = 0

    def _read_file_(self):
        """Reads the file and puts the lines in a hash"""
        with open(self.input_file) as open_file:
            self.desired_count = int(open_file.readline())
            for line in open_file.readlines():
                line = line.strip()
                key = len(line)
                self.lengths[key].append(line)

    def _get_results_(self):
        """Gets the desired number of lines"""
        keys = sorted(self.lengths.keys(), reverse=True)
        result = []
        for key in keys:
            result += self.lengths[key]
            if len(result) >= self.desired_count:
                break
        return result

    def run(self):
        self._read_file_()
        return self._get_results_()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Invalid arguments")
    else:
        ll = LongestLines(sys.argv[1])
        results = ll.run()
        for result in results:
            print(result)
