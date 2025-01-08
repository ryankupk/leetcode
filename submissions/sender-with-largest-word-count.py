from collections import defaultdict
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sender_words = defaultdict(int)

        for sender, message in zip(senders, messages):
            sender_words[sender] += len(message.split(' '))

        potential = []
        most = -1

        for sender, words in sender_words.items():
            if words > most:
                potential = [sender]
                most = words
            elif words == most:
                potential.append(sender)
        
        return max(potential)
