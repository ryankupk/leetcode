// https://leetcode.com/problems/number-of-good-pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num == num2: pairs += 1
                
                
        return pairs
                
        