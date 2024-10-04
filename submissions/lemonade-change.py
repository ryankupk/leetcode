# https://leetcode.com/problems/lemonade-change

from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change = defaultdict(int)
        for bill in bills:
            if bill == 5:
                change[5] += 1
                continue
                
            if bill == 10 and change[5] > 0:
                change[10] += 1
                change[5] -= 1
                continue
            
            if bill == 10 and change[5] == 0:
                return False

            if bill == 20 and ((change[10] > 0 and change[5] > 0)):
                change[5] -= 1
                change[10] -= 1
                change[20] += 1
                continue

            if bill == 20 and ((change[5] >= 3)):
                change[5] -= 3
                change[20] += 1
                continue

            if bill == 20:
                return False
        
        return True
                
        