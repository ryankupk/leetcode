# https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for idx, letter in enumerate(columnTitle):
            total += (ord(letter) - 64) * 26 ** (len(columnTitle) - 1 - idx)
        return total
        