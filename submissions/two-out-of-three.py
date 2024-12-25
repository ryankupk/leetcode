from collections import Counter
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        set_one, set_two, set_three = set(nums1), set(nums2), set(nums3)

        res = set()
        res = res.union(set_one.intersection(set_two))
        res = res.union(set_one.intersection(set_three))
        res = res.union(set_two.intersection(set_three))
        return list(res)
