class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def total(k):
            return k * costBoth + max(0, need1 - k) * cost1 + max(0, need2 - k) * cost2
        return min(total(0), total(need1), total(need2))