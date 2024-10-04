# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i

from collections import Counter
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        ops = 0
        for num, count in counts.items():
            if num < k:
                ops += count
        return ops
        
        