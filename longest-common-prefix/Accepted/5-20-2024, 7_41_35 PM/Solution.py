// https://leetcode.com/problems/longest-common-prefix

from functools import reduce
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def pair_prefix(a, b):
            longest_common_prefix = ""
            for char1, char2 in zip(a, b):
                if char1 == char2:
                    longest_common_prefix += char1
                else:
                    return longest_common_prefix

            return longest_common_prefix

        return reduce(pair_prefix, strs)