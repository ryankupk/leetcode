# https://leetcode.com/problems/crawler-log-folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for operation in logs:
            if operation == './':
                continue
            if operation == '../' and depth > 0:
                depth -= 1
                continue
            if operation == '../' and depth <= 0:
                depth = 0
                continue


            depth += 1
                
        return depth
        