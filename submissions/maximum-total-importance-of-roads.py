# https://leetcode.com/problems/maximum-total-importance-of-roads

from collections import defaultdict
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        visited = []
        num_roads_connecting = defaultdict(int)
        assignments = {}
        total = 0
        
        for road in roads:
            num_roads_connecting[road[0]] += 1
            num_roads_connecting[road[1]] += 1

        assignment = n
        for city, count in sorted(num_roads_connecting.items(), key=lambda x: x[1], reverse=True):
            assignments[city] = assignment
            assignment -= 1
            
        for road in roads:
            total += assignments[road[0]] + assignments[road[1]]

        return total
        