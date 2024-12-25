from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        valid = [str(num) for num in range(100, 1000, 2)]

        res = []
        digits_counts = Counter(digits)
        for num in valid:
            continue_outer = False
            num_counts = Counter([int(cur_num) for cur_num in num])
            for cur_num, count in num_counts.items():
                if cur_num not in digits or count > digits_counts[cur_num]:
                    continue_outer = True
                    break
            if continue_outer:
                continue
            res.append(int(num))

        return res
