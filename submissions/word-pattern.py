# https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        mapping = {}
        for letter, word in zip(pattern, words):
            if letter in mapping and mapping[letter] != word:
                return False
            if letter not in mapping and word in mapping.values():
                return False
            mapping[letter] = word
        
        return True
            
        