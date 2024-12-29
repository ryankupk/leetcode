from collections import Counter
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for num in sorted(counts.keys(), reverse=True):
            if -num in counts:
                return num
        
        return -1
