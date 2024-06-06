// https://leetcode.com/problems/left-and-right-sum-differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []
        for idx, _ in enumerate(nums):
            result.append(abs(
                sum(nums[:idx+1]) - sum(nums[idx:])
            ))

        return result
        