class Solution:
    def findPattern(self, s):
        n = len(s)
        i = 0
        while i < n:
            if s[i] != 'x':
                return False
            a = 0
            while i < n and s[i] == 'x':
                a += 1
                i += 1
            b = 0
            while i < n and s[i] == 'y':
                b += 1
                i += 1
            if a != b:
                return False
        return True