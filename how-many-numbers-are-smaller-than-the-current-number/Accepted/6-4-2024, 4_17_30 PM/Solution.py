// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i, num in enumerate(nums):
            for num2 in nums:
                if num2 < num:
                    result[i] += 1
        return result
        