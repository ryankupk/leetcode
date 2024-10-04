# https://leetcode.com/problems/sum-of-square-numbers

from math import floor
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0: return True
        up = 0
        down = floor(c ** 0.5)+1

        while up < floor(c ** 0.5)+1 and down > 0:
            square_sum = up ** 2 + down ** 2
            if square_sum == c:
                return True
            
            if square_sum < c:
                up += 1
            elif square_sum > c:
                down -= 1
                
        return False
        