# https://leetcode.com/problems/keyboard-row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            'zxcvbnm',
            'asdfghjkl',
            'qwertyuiop'
        ]
        result = []
        for word in words:
            letters = set([letter.lower() for letter in word])
            for row in rows:
                for letter in letters:
                    if letter not in row:
                        break
                else:
                    result.append(word)
        
        return result

        