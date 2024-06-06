# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        def generate_subsets(nums, index, current_subset, subsets):
            if index == len(nums):
                subsets.append(current_subset[:])
                return
            
            current_subset.append(nums[index])
            generate_subsets(nums, index + 1, current_subset, subsets)
            current_subset.pop()
            generate_subsets(nums, index + 1, current_subset, subsets)


        generate_subsets(nums, 0, [], subsets)
        return subsets