// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([jewel for jewel in stones if jewel in jewels])
        