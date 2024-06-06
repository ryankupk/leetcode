// https://leetcode.com/problems/the-number-of-beautiful-subsets

from functools import reduce
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        subsets = 0
        if len(nums) == 1:
            return 1
        
        def is_beautiful(subset):
            for num in subset:
                if (num + k) in subset or (num - k) in subset: 
                    return False

            return True

        def generate_subsets(nums, cur_subset, index):

            if index == len(nums):
                if len(cur_subset) > 0 and is_beautiful(cur_subset[:]):
                    nonlocal subsets
                    subsets += 1
                return

            cur_subset.append(nums[index])
            generate_subsets(nums, cur_subset, index+1)
            cur_subset.pop()
            generate_subsets(nums, cur_subset, index+1)

        nums.sort()
        generate_subsets(nums, [], 0)
        return subsets