import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            heapq.heappush(res, -num)
        for i in range(k-1):
            heapq.heappop(res)
        return -heapq.heappop(res)
