class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(x):
            stack = []
            for ch in x:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack
        return build(s) == build(t)