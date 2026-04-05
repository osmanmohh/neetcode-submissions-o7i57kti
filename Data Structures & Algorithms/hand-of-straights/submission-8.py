class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        count = collections.Counter(hand)
        for num in hand:
            if num not in count:
                continue
            for i in range(groupSize):
                if num + i not in count:
                    return False
                count[num + i] -= 1
                if count[num + i] == 0:
                    del count[num + i]
        return True