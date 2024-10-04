# https://leetcode.com/problems/hand-of-straights

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        
        hand.sort()

        while hand:
            lowest = min(hand)
            needed_cards = [lowest + i for i in range(groupSize)]
            for needed_card in needed_cards:
                try:
                    hand.remove(needed_card)
                except:
                    return False
                
        return True

        