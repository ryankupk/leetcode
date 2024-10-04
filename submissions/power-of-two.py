# https://leetcode.com/problems/power-of-two

from math import floor
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n in [2 ** i for i in range(100)]
        