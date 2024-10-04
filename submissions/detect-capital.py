# https://leetcode.com/problems/detect-capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        
        # case 1 - all uppercase
        if word == ''.join([letter.upper() for letter in word]):
            return True
        
        # case 2 - all lowercase
        if word == ''.join([letter.lower() for letter in word]):
            return True
        
        # case 3 - title case
        if word[0] == word[0].upper() and word[1:] == ''.join([letter.lower() for letter in word[1:]]):
            return True

        return False
        