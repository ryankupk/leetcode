# https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [''] * n
        for i in range(1, n+1):
            cur = ''
            if i % 3 == 0:
                cur += 'Fizz'
            if i % 5 == 0:
                cur += 'Buzz'
            if len(cur) == 0:
                cur = str(i)
            answer[i-1] = cur
        return answer
        