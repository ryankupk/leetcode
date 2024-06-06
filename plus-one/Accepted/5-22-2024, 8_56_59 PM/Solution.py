// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # stringed = [str(digit) for digit in digits]
        # joined = ''.join(stringed)
        # inted = int(joined)
        # incremented = inted + 1
        # return [digit for digit in str(incremented)]
        return [int(digit) for digit in str(int(''.join([str(digit) for digit in digits])) + 1)]
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        index = len(digits) - 1
        carry = False
        while index >= 0 and digits[index] == 9:
            digits[index] = 0
            carry = True
            index -= 1

        if carry:
            digits[index] += 1
        return digits