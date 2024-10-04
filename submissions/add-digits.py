# https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        
        while len(num) > 1:
            num = str(sum((int(digit) for digit in num)))
            
        return int(num)
        