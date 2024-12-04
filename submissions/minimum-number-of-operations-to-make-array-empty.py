#
# @lc app=leetcode id=2870 lang=python3
#
# [2870] Minimum Number of Operations to Make Array Empty
#

# @lc code=start
from collections import Counter
import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        num_changes = 0

        for _, count in counts.items():
            if count == 1:
                return -1
            remove_threes = math.floor(count / 3)
            remainder = count % 3
            if remainder == 0:
                pass
            elif remainder == 1:
                remove_threes -= 1
                remove_threes += 2
            elif remainder == 2:
                remove_threes += 1
            num_changes += remove_threes

        return num_changes
        
# @lc code=end

