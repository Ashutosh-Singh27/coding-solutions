from collections import deque

class Solution:
    def getCount(self, root, k):
        if not root:
            return 0

        costs = []
        q = deque([(root, 1)])

        while q:
            node, level = q.popleft()
            if not node.left and not node.right:
                costs.append(level)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        costs.sort()

        count = 0
        total = 0
        for c in costs:
            if total + c > k:
                break
            total += c
            count += 1

        return count