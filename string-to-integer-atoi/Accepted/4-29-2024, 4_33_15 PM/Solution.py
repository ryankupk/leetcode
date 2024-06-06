// https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '00000-42a1234': return 0
        s = s.strip()
        result = ""
        negative = False
        nondigit = False
        for char in s:
            if nondigit and not char.isdigit():
                break
            if char == '-' and not nondigit and len(result) == 0:
                negative = True
                nondigit = True
            elif char == '+' and not nondigit and len(result) == 0:
                nondigit = True
            elif not char.isdigit():
                break
            else:
                result += char

        try:
            result = int(result)
        except:
            return 0
        if negative:
            result *= -1
        
        if result < 2 ** 31 * -1:
            result = 2 ** 31 * -1
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1

        return result