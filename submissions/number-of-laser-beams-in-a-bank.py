# https://leetcode.com/problems/number-of-laser-beams-in-a-bank

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        beams = 0
        for i in range(len(bank[:-1])):
            j = i + 1
            row1 = bank[i]
            # print(f"{row1=}")
            while j < len(bank)-1 and '1' not in bank[j]:
                j += 1

            row2 = bank[j]
            # print(f"{row2=}")

            beams += sum((1 for _ in filter(lambda x: x == '1', row1))) * sum((1 for _ in filter(lambda x: x == '1', row2)))
            # print(f"{beams=}")

        return beams
        