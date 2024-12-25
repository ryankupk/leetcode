class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, val in enumerate(sorted(nums)) if val == target]
