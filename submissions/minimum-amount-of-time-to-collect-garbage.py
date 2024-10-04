# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time_taken = 0
        latest_m = 0
        latest_p = 0
        latest_g = 0
        for idx, house in enumerate(garbage):
            time_taken += len(house)
            if "M" in house:
                latest_m = idx
            if "P" in house:
                latest_p = idx
            if "G" in house:
                latest_g = idx
        
        for idx, time in enumerate(travel):
            if idx < latest_m:
                time_taken += time
            if idx < latest_p:
                time_taken += time
            if idx < latest_g:
                time_taken += time

        return time_taken
        