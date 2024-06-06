// https://leetcode.com/problems/most-common-word

from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = Counter(re.findall(r'\w+', paragraph.lower()))
        # print(counts)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        # sorted_counts = sorted(counts, key=lambda x: )
        # print(sorted_counts)
        for word, freq in sorted_counts:
            if word not in banned:
                return word
        