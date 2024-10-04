# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num + num2 < target:
                    count += 1
        return count
        