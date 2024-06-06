// https://leetcode.com/problems/find-the-number-of-good-pairs-i

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = 0
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1 % (num2 * k) == 0:
                    pairs += 1
        
        return pairs
                