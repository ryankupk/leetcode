#
# @lc app=leetcode id=3120 lang=python3
#
# [3120] Count the Number of Special Characters I
#

# @lc code=start
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        res = 0
        for letter in letters:
            if letter in word and letter.upper() in word:
                res += 1

        return res
        
# @lc code=end

