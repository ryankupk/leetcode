# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k

from functools import reduce
from collections import Counter

class Solution:
    def xorElems(self, nums: List[int]) -> int:

        return reduce(lambda x, y: x^y, nums)
    def minOperations(self, nums: List[int], k: int) -> int:
        
        # starting = self.xorElems(nums)
        # xor = starting^k
        # counts = Counter(bin(xor))
        return Counter(bin(reduce(lambda x, y: x^y, nums)^k))['1']
