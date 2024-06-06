// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and target in nums:
            return [0,0]
        starting = None
        try:
            starting = nums.index(target)
        except:
            return [-1,-1]
        print(starting)
        for idx, num in enumerate(nums[starting:]):
            if (num == target and idx + starting + 1 < len(nums) and nums[idx + starting + 1] != target) or idx + starting + 1 >= len(nums):
                return [starting, starting + idx]