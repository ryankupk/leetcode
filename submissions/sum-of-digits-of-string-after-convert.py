# https://leetcode.com/problems/sum-of-digits-of-string-after-convert

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        as_string = ''.join((str(ord(letter) - 96) for letter in s))
        def transform(s: str):
            num = sum((int(letter) for letter in s))
            new_s = str(num)
            return new_s

        for _ in range(k):
            as_string = transform(as_string)

        return int(as_string)