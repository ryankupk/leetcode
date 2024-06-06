# https://leetcode.com/problems/sum-of-all-subset-xor-totals

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        xor_sum = 0
        subsets = []
        def generate_subsets(nums, current_subset, index, subsets):
            if index == len(nums):
                subsets.append(current_subset[:])
                return

            current_subset.append(nums[index])
            generate_subsets(nums, current_subset, index + 1, subsets)

            current_subset.pop()
            generate_subsets(nums, current_subset, index + 1, subsets)

        generate_subsets(nums, [], 0, subsets)
        for arr_subset in subsets:
            if len(arr_subset) > 0:
                xor_sum += reduce(lambda x, y: x ^ y, arr_subset)

        return xor_sum