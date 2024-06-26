# https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[self.k * -1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)