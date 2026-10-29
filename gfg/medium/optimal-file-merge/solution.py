import heapq

class Solution:
    def minComputation(self, files):
        heapq.heapify(files)
        total = 0
        while len(files) > 1:
            a = heapq.heappop(files)
            b = heapq.heappop(files)
            total += a + b
            heapq.heappush(files, a + b)
        return total