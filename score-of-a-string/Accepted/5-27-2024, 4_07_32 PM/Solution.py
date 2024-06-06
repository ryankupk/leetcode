// https://leetcode.com/problems/score-of-a-string

class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for idx, letter in enumerate(s[:-1]):
            total += abs(ord(letter) - ord(s[idx + 1]))
        return total
        