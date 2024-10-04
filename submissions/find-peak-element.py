# https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        for idx, num in enumerate(nums[1:], 1):
            if nums[idx-1] < num > nums[idx+1]:
                return idx

            
        