// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(digit) for digit in str(int(''.join([str(digit) for digit in digits])) + 1)]
