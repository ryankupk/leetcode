# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix

class Solution:
    #                                n                m
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set1 = set()
        for num in arr1:
            strung = str(num)
            for i in range(1, len(strung)+1):
                set1.add(strung[:i])
        
        longest_prefix = ''
        
        for num in arr2:
            strung = str(num)
            for i in range(1, len(strung)+1):
                prefix = strung[:i]
                if prefix in set1 and len(prefix) > len(longest_prefix):
                    longest_prefix = prefix

        print(f"{longest_prefix=}")
        print(f"{set1=}")

        return len(longest_prefix)
                    
        
        