# https://leetcode.com/problems/split-a-string-in-balanced-strings

from collections import Counter
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_substrs = 0
        balanced = 0
        for letter in s:
            if letter == 'L':
                balanced += 1
            elif letter == 'R':
                balanced -= 1
            else:
                exit()

            if balanced == 0:
                num_substrs += 1

        return num_substrs