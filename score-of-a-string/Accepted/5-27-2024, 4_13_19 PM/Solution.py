// https://leetcode.com/problems/score-of-a-string

from functools import reduce
class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for idx, _ in enumerate(s[:-1]):
            total += abs(ord(s[idx]) - ord(s[idx + 1]))
        return total
        