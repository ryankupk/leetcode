# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k

from functools import reduce

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for letter in bin(reduce(lambda x, y: x^y, nums)^k):
            if letter == '1': count += 1

        return count
        return len([ letter for letter in bin(reduce(lambda x, y: x^y, nums)^k) if letter == '1' ])
