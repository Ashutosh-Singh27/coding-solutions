class Solution:
    def checkStatus(self, a, b, flag):
        cond1 = ((a >= 0) != (b >= 0)) and not flag
        cond2 = (a < 0 and b < 0) and flag
        return cond1 or cond2