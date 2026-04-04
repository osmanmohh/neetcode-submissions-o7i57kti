class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tank = 0
        total = 0
        for i in range(len(cost)):
            diff = gas[i] - cost[i]
            tank += diff
            total += diff
            if tank < 0:
                tank = 0
                start = i + 1
        return start if total >= 0 else -1
            

        