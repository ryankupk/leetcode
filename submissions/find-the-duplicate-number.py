#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for k, v in Counter(nums).items():
            if v >= 2:
                return k
        
# @lc code=end

