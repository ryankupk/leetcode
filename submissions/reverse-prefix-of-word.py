# https://leetcode.com/problems/reverse-prefix-of-word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pivot = word.find(ch)
        if pivot == -1: return word
        
        return ''.join([letter for letter in reversed(word[0:pivot+1])]) + word[pivot+1:]
        