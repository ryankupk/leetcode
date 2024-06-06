// https://leetcode.com/problems/number-of-employees-who-met-the-target

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum((1 for _ in filter(lambda x: x >= target, hours)))
        