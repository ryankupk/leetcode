// https://leetcode.com/problems/find-the-original-array-of-prefix-xor

from functools import reduce
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        for idx, _ in enumerate(pref[1:], 1):
            # arr.append(reduce(lambda x, y: x ^ y, pref[0:idx]))
            arr.append(pref[idx] ^ pref[idx-1])

        return arr
            
        