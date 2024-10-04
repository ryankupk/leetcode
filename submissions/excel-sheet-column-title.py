# https://leetcode.com/problems/excel-sheet-column-title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            res = chr(65 + columnNumber % 26) + res
            columnNumber //= 26
        return res
        