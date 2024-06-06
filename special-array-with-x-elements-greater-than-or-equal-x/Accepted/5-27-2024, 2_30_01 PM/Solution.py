# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

from collections import Counter
class Solution:
    def specialArray(self, nums: List[int]) -> int:

        return [len([num for num in nums if num >= i]) for i in range(0, len(nums) + 1) if len([num for num in nums if num >= i]) == i][0] if len([len([num for num in nums if num >= i]) for i in range(0, len(nums) + 1) if len([num for num in nums if num >= i]) == i]) > 0 else -1