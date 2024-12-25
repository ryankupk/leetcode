class Solution:
    def countEven(self, num: int) -> int:
        return sum(1 for i in range(1, num+1) if sum(int(num) for num in str(i)) % 2 == 0)
        count = 0
        for i in range(1, num+1):
            if sum(int(num) for num in str(i)) % 2 == 0:
                count += 1

        return count
