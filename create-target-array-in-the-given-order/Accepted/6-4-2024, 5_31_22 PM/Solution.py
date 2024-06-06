# https://leetcode.com/problems/create-target-array-in-the-given-order

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for num, idx in zip(nums, index):
            target.insert(idx, num)
        return target
        