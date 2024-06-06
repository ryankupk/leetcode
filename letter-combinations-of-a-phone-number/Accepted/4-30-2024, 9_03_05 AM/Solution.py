# https://leetcode.com/problems/letter-combinations-of-a-phone-number

from itertools import permutations
from functools import reduce
class Solution:
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        if len(digits) == 1: return [letter for letter in self.letters[digits]]

        combinations = []
        def backtrack(start, path):
            if len(path) == len(digits):
                combinations.append(''.join(path))
            else:
                for letter in self.letters[digits[start]]:
                    path.append(letter)
                    backtrack(start + 1, path)
                    path.pop()

        backtrack(0, [])
        return combinations
