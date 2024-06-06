# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k

from functools import reduce
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return Counter(bin(reduce(lambda x, y: x^y, nums)^k))['1']
