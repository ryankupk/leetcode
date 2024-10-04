# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        result = 0
        for idx, num in enumerate(nums):
            if len([bit for bit in bin(idx) if bit == '1']) == k:
                result += num
                
        return result
        