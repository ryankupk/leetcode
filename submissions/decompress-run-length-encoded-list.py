# https://leetcode.com/problems/decompress-run-length-encoded-list

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new = []
        i = 0
        while i < len(nums)-1:
            # print(f"{i=}")
            new.extend([nums[i+1]] * nums[i])
            
            i += 2

        return new
        