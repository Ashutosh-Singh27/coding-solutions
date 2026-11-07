class Solution:
    def countValidSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        last=-1
        for j in range(n):
            if j>=2 and s[j-2:j+1]=="abc":
                last=j-2
            ans +=j-last
        return ans