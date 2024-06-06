// https://leetcode.com/problems/decode-xored-array

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for idx, num in enumerate(encoded):
            arr.append(arr[idx] ^ num)
        
        return arr
        