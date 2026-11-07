class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        reserved = set(arr)    
        assigned = set()       
        nxt = {}               
        res = []
        for name in arr:
            if name not in assigned:
                assigned.add(name)
                res.append(name)
            else:
                k = nxt.get(name, 1)
                while (name + str(k)) in reserved or (name + str(k)) in assigned:
                    k += 1
                new = name + str(k)
                nxt[name] = k + 1  
                assigned.add(new)
                res.append(new)
        return res