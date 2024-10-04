# https://leetcode.com/problems/continuous-subarray-sum

from itertools import accumulate
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        mod_dict = {0: -1}  
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            mod_value = prefix_sum % k
            if mod_value < 0:
                mod_value += k

            if mod_value in mod_dict:
                if i - mod_dict[mod_value] > 1:
                    return True
            else:
                mod_dict[mod_value] = i

        return False