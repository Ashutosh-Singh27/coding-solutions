class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        groups = {}
        for a in range(n):
            for b in range(a + 1, n):
                groups.setdefault(arr[a] + arr[b], []).append((a, b))

        best = None
        for lst in groups.values():
            if len(lst) < 2:
                continue
            # lst is already sorted lexicographically
            if best is not None and lst[0] > best[:2]:
                continue
            found = False
            for i in range(len(lst)):
                a, b = lst[i]
                if best is not None and (a, b) > best[:2]:
                    break
                for j in range(i + 1, len(lst)):
                    c, d = lst[j]
                    if c != a and c != b and d != a and d != b:
                        cand = (a, b, c, d)
                        if best is None or cand < best:
                            best = cand
                        found = True
                        break
                if found:
                    break

        return list(best) if best else [-1, -1, -1, -1]