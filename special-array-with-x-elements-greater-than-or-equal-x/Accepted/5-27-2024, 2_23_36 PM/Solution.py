// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

from collections import Counter
class Solution:
    def specialArray(self, nums: List[int]) -> int:

        # counted = Counter(nums)
        # print(f"{counted=}")

        # smallest = min(counted.keys())
        for i in range(0, len(nums) + 1):
            count_i = 0
            for num in nums:
                if num >= i:
                    count_i += 1
            if count_i == i:
                return count_i

        return -1