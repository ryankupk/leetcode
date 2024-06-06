// https://leetcode.com/problems/shuffle-the-array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [x for i in range(n) for x in (nums[i], nums[i+n])]
        shuffled = []
        for i in range(n):
            shuffled.append(nums[i])
            shuffled.append(nums[i + n])
        return shuffled
        