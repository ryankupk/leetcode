# https://leetcode.com/problems/two-sum

from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # complement = defaultdict(0)
        # complements = []
        complements = {}

        for idx, num in enumerate(nums):
            if num in complements:
                return [complements[num], idx]
            
            complements[target - num] = idx
