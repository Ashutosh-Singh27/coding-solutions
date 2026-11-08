class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res=[]
        n=len(s1)
        i=0
        while i<n:
            if s1[i]!=s2[i]:
                j=i
                while j<n and s1[j]!=s2[j]:
                    j+=1
                res.append([s1[i:j], s2[i:j]])
                i=j
            else:
                i+=1
        return res