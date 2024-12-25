class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        return all([int(a) < int(b) for a, b in zip([word for word in s.split(' ') if word[0].isdigit()][:-1], [word for word in s.split(' ') if word[0].isdigit()][1:])])
        nums = [word for word in s.split(' ') if word[0].isdigit()]

        for a, b in zip(nums[:-1], nums[1:]):
            if int(a) >= int(b):
                return False

        return True
