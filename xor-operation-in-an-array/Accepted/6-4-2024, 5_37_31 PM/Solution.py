// https://leetcode.com/problems/xor-operation-in-an-array

from functools import reduce
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        for i in range(n):
            nums[i] = start + 2 * i
        
        return reduce(lambda x, y: x ^ y, nums)
        