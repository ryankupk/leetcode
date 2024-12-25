class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        count = 0
        for i, val_one in enumerate(nums):
            for j, val_two in enumerate(nums[i+1:]):
                if abs(val_one - val_two) == k:
                    count += 1

        return count
