// https://leetcode.com/problems/k-th-smallest-prime-fraction

class Solution(object):
    def sortOrder(self, fraction):
        return float(fraction[0]) / float(fraction[1])
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        fractions = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fractions.append([arr[i], arr[j]])
        
        return sorted(list(fractions), key=(lambda x: float(x[0]) / float(x[1])))[k-1]