// https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return len([1 for n in operations if '-' in n]) * - 1 + len([1 for n in operations if '+' in n])
        x = 0
        for operation in operations:
            if '-' in operation: x -= 1
            else: x += 1
        return x
        