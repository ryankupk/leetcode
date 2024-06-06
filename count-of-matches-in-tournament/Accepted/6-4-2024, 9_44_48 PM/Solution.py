// https://leetcode.com/problems/count-of-matches-in-tournament

class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        while n > 1:
            matches = n // 2
            remainder = n % 2
            total_matches += matches
            n = matches + remainder

        return total_matches
            
        