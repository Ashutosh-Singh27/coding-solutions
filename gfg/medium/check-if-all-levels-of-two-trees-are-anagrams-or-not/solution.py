from collections import deque, Counter

class Solution:
    def areAnagrams(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            if len(q1) != len(q2):
                return False

            c1 = Counter()
            c2 = Counter()

            for _ in range(len(q1)):
                a = q1.popleft()
                b = q2.popleft()

                c1[a.data] += 1
                c2[b.data] += 1

                if a.left:
                    q1.append(a.left)
                if a.right:
                    q1.append(a.right)
                if b.left:
                    q2.append(b.left)
                if b.right:
                    q2.append(b.right)

            if c1 != c2:
                return False

        return not q1 and not q2