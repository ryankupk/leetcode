# https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels = ['a','e','i','o','u']
        vowels = 'aeiuoAEIOU'
        s_no_vowels = [letter for letter in s if letter not in vowels]
        s_vowels_idx = {}
        
        for idx, letter in enumerate(s):
            if letter in vowels:
                s_vowels_idx[idx] = letter

        s_vowels = ''.join(s_vowels_idx.values())[::-1]

        for idx, letter in zip(s_vowels_idx.keys(), s_vowels):
            s_no_vowels.insert(idx, letter)

        return ''.join(s_no_vowels)


        