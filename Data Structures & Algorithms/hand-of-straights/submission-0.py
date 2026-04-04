class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = collections.Counter(hand)
        hand.sort()
        for num in hand:
            if counter[num] > 0:
                for i in range(num, num + groupSize):
                    if counter[i] == 0:
                        return False
                    counter[i] -= 1
        return True


        