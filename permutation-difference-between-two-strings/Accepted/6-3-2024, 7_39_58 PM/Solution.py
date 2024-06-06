// https://leetcode.com/problems/permutation-difference-between-two-strings

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        perm_diff = 0
        for idx, letter in enumerate(s):
            perm_diff += abs(idx - t.find(letter))
        return perm_diff
        