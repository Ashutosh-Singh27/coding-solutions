class Solution:
    def maxPathSum(self, root):
        self.best = float('-inf')

        def dfs(node):
            if not node:
                return float('-inf')
            if not node.left and not node.right:
                return node.data
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.right:
                self.best = max(self.best, left + right + node.data)
                return node.data + max(left, right)
            if node.left:
                return node.data + left
            return node.data + right

        dfs(root)
        return -1 if self.best == float('-inf') else self.best