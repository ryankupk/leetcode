# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        new_num = int(str(x)[::-1]) if x >= 0 else int(str(x)[1:][::-1]) * -1
        if new_num < 2 ** 31 * -1 or new_num > 2 ** 31 - 1:
            return 0
        return new_num