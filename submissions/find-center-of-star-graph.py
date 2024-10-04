# https://leetcode.com/problems/find-center-of-star-graph

from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        counts = Counter(edges[0] + edges[1])
        for node, count in counts.items():
            if count > 1:
                return node
        
        