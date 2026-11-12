class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        best = float('inf')
        node = root
        while node:
            best = min(best, abs(node.data - k))
            if best == 0:
                return 0
            if k < node.data:
                node = node.left
            else:
                node = node.right
        return best