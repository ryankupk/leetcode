// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurrences = {}
        n = len(nums)
        for num in nums:
            if num not in occurrences:
                occurrences[num] = 1
            else:
                occurrences[num] += 1
                if occurrences[num] > n//2:
                    return num
        for num, count in occurrences.items():
            if count > n//2:
                return num