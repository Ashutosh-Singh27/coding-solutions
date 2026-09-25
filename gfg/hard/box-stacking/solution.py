class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        n = len(height)
        boxes = []

        for i in range(n):
            h, w, l = height[i], width[i], length[i]
            boxes.append((w, l, h))
            boxes.append((h, l, w))
            boxes.append((h, w, l))

        def normalize(box):
            w, l, h = box
            if w < l:
                w, l = l, w
            return (w, l, h)

        boxes = [normalize(b) for b in boxes]
        boxes.sort(key=lambda x: x[0] * x[1], reverse=True)

        m = len(boxes)
        dp = [boxes[i][2] for i in range(m)]

        for i in range(1, m):
            for j in range(i):
                if boxes[j][0] > boxes[i][0] and boxes[j][1] > boxes[i][1]:
                    if dp[j] + boxes[i][2] > dp[i]:
                        dp[i] = dp[j] + boxes[i][2]

        return max(dp)