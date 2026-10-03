class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        m = 4 * n
        moves = [m - 1]
        k = m - 2
        while k > 0:
            moves.extend([k, k])
            k -= 2

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        r = c = 0
        first = [1]
        for i, length in enumerate(moves):
            dr, dc = dirs[i % 4]
            for _ in range(length):
                r += dr
                c += dc
                first.append(r * m + c + 1)

        total = m * m + 1
        second = [total - x for x in first]
        return [first, second]