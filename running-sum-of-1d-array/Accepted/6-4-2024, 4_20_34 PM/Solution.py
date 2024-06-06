// https://leetcode.com/problems/running-sum-of-1d-array

from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)
        result = []
        for i, num in enumerate(nums):
            result.append(sum(nums[:i+1]))
        
        return result