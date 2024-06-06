// https://leetcode.com/problems/single-number-ii

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return [item for item in counts if counts[item] == 1][0]
        