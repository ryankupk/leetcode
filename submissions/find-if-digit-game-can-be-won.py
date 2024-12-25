class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(num for num in nums if num < 10) != sum(num for num in nums if num >= 10)
