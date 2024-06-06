# https://leetcode.com/problems/the-number-of-beautiful-subsets

from functools import reduce
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        subsets = 0
        if len(nums) == 1:
            return 1
        
        def is_beautiful(subset):
            for num in subset:
                if (num + k) in subset or (num - k) in subset: # make faster
                    return False

            return True

        def generate_subsets(nums, cur_subset, index):

            if index == len(nums):
                if is_beautiful(cur_subset[:]) and len(cur_subset) > 0:
                    # print(f"{cur_subset=}")
                    nonlocal subsets
                    subsets += 1
                    # print(f"{subsets=}")
                return

            cur_subset.append(nums[index])
            generate_subsets(nums, cur_subset, index+1)
            cur_subset.pop()
            generate_subsets(nums, cur_subset, index+1)

        # nums.sort()
        generate_subsets(nums, [], 0)
        return subsets