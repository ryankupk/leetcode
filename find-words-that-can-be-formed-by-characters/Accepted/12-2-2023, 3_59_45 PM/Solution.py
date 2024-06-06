# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_lengths = 0
        char_counts = Counter(chars)
        for word in words:
            word_counts = Counter(word)
            for char, count in word_counts.items():
                if char not in char_counts or char_counts[char] < count:
                    break
            else: total_lengths += len(word)

        return total_lengths


"""
{
    a: 2,
    t: 1,
    c: 1,
    h: 1
}
{
    c: 1,
    a: 1,
    t: 1
}
"""