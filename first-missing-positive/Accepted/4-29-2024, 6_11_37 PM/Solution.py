// https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        smallest = 1
        for num in nums:
            if num <= 0:
                continue
            if num > smallest:
                return smallest
            smallest += 1
        return smallest