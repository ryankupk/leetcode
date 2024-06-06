# https://leetcode.com/problems/find-common-characters

from functools import reduce
from collections import Counter, defaultdict
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        word_counts = [Counter(word) for word in words]
        common_chars = reduce(lambda x, y: x & y, word_counts)
        return list(common_chars.elements())
        