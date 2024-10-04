# https://leetcode.com/problems/number-complement

class Solution:
    def findComplement(self, num: int) -> int:
        bits = bin(num)[2:]
        complement = ''
        for bit in bits:
            complement += str(abs(int(bit)-1))
        return int(complement, 2)
            

        # return int(''.join([abs(int(i)-1) for i in bin(num)[2:]]), 2)
        