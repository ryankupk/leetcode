// https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            result.append(sum(nums[:i+1]))
        
        return result