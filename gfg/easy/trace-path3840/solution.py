class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        x = y = 0
        min_x = max_x = min_y = max_y = 0
        for c in s:
            if c == 'L':
                x -= 1
            elif c == 'R':
                x += 1
            elif c == 'D':
                y -= 1
            elif c == 'U':
                y += 1
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        return (max_x - min_x) < m and (max_y - min_y) < n