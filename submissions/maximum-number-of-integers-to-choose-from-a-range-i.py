#
# @lc app=leetcode id=2554 lang=python3
#
# [2554] Maximum Number of Integers to Choose From a Range I
#

# @lc code=start
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        if maxSum == 0:
            return 0

        banned = set(banned)

        if maxSum == 1:
            if 1 not in banned:
                return 1
            else:
                return 0

        count = 0
        cur = 0

        for num in (num for num in range(1, n+1) if num not in banned):
            cur += num
            count += 1
            if cur > maxSum:
                cur -= num
                count -= 1
                return count
            if cur == maxSum:
                return count
        
        return count
        
# @lc code=end

