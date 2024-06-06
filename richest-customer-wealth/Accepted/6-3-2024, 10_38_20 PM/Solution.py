# https://leetcode.com/problems/richest-customer-wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        most = 0
        for account in accounts:
            most = max(sum(account), most)
            
        return most
        