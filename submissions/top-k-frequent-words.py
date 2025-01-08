from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)

        freqs = [[] for _ in range(max(counts.values())+1)]

        for word, count in counts.items():
            freqs[count].append(word)

        res = []
        for ls in reversed(freqs):
            if k <= 0:
                break
            res.extend(sorted(ls)[:k])
            k -= len(ls)
        return res
