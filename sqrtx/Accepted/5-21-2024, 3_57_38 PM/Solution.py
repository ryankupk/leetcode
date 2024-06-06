// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1
        if x == 2: return 1
        for i in range(0, x):
            if i * i == x:
                return i
            if i * i > x:
                return i-1