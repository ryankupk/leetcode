class Solution:
    def checkString(self, s: str) -> bool:
        return 'ba' not in s
        for i, letter in enumerate(s):
            if letter == 'a':
                continue
            elif letter == 'b':
                for letter_two in s[i+1:]:
                    if letter_two == 'a':
                        return False
                    
        return True
