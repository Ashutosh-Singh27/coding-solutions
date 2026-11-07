class Solution:
    def countValidSubstrings(self, s: str) -> int:
        A=B=C=-1
        ans=0
        for i,ch in enumerate(s):
            if ch=='a':
                A=i
            elif ch=='b':
                B=A
            else:
                C=B
            ans+=i-C
        return ans