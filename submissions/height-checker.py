# https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        indices = 0
        for height, expected in zip(heights, sorted(heights)):
            if height != expected:
                indices += 1
        
        return indices
        