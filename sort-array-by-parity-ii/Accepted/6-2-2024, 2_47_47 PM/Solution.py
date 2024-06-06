// https://leetcode.com/problems/sort-array-by-parity-ii

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums