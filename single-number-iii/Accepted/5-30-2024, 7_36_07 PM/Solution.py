# https://leetcode.com/problems/single-number-iii

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return [item for item in counts if counts[item] == 1]
        