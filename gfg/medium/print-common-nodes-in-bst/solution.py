class Solution:
    def findCommon(self, r1, r2):
        def inorder(root):
            res = []
            stack = []
            cur = root
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                res.append(cur.data)
                cur = cur.right
            return res

        a = inorder(r1)
        b = inorder(r2)
        i = j = 0
        ans = []
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                ans.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return ans