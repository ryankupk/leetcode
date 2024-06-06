# https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(start, curr_partition):
            if start == len(s):
                result.append(curr_partition[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    curr_partition.append(s[start:end+1])
                    backtrack(end + 1, curr_partition)
                    curr_partition.pop()

        result = []
        backtrack(0, [])
        return result
