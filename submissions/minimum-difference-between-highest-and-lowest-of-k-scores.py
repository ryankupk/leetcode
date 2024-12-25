class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return abs(nums[1] - nums[0])
        if k == 1:
            return 0
        smallest = float('inf')
        nums.sort()
        for a, b in zip(nums[:-k+1], nums[k-1:]):
            smallest = min(smallest, b - a)

        return smallest
