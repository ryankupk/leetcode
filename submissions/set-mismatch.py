# https://leetcode.com/problems/set-mismatch

from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        double = None
        for num, count in counts.items():
            if count == 2:
                double = num
                break
        
        for num in range(1, len(nums)+1):
            if num not in nums:
                return [double, num]


                

            
        