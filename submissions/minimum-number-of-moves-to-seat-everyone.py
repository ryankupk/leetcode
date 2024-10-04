# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        total_moves = 0
        seats.sort()
        students.sort()
        for student, seat in zip(students, seats):
            total_moves += abs(student - seat)

        return total_moves
        