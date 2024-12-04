#
# @lc app=leetcode id=2825 lang=python3
#
# [2825] Make String a Subsequence Using Cyclic Increments
#

# @lc code=start
class Solution:

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def increment(char: str) -> str:
            mutated = chr(ord(char) + 1)
            if mutated == chr(ord('z') + 1):
                mutated = 'a'
            return mutated

        i, j = 0, 0

        while j < len(str2) and i < len(str1):
            if str1[i] == str2[j] or increment(str1[i]) == str2[j]:
                i += 1
                j += 1
            else:
                i += 1
            
        if j == len(str2):
            return True
        return False
        
# @lc code=end

