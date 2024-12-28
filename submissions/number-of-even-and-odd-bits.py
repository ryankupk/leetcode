class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res = [0,0]
        for i, val in enumerate(reversed(bin(n)[2:])):
            if i % 2 == 0 and val == '1':
                res[0] += 1
            elif i % 2 == 1 and val == '1':
                res[1] += 1
        return res
