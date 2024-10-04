# https://leetcode.com/problems/minimum-number-game

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        arr = []
        i = 0
        while i < len(nums):
            alice = sorted_nums[i]
            bob = sorted_nums[i+1]
            arr.append(bob)
            arr.append(alice)

            i += 2

        return arr

        