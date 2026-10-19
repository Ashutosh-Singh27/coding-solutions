class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        state = [0] * n
        for i in range(n):
            if state[i]:
                continue
            path = []
            cur = i
            while True:
                if cur < 0 or cur >= n:
                    res = 2
                    break
                if state[cur] == 1:
                    res = 3
                    break
                if state[cur] != 0:
                    res = state[cur]
                    break
                state[cur] = 1
                path.append(cur)
                cur += arr[cur]
            for p in path:
                state[p] = res
        return state.count(2)