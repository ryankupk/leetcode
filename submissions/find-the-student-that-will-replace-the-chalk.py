# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        i = 0
        n = len(chalk)
        total_chalk = sum(chalk)

        k %= total_chalk

        while True:
            if k < chalk[i]:
                return i
        
            k -= chalk[i]
            i = (i + 1) % n
        
        return i