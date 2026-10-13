class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
        diff = [0] * (n + 1)
        for j in updates:
            diff[j - 1] += 1
        res = []
        running = 0
        for i in range(n):
            running += diff[i]
            res.append(running)
        return res