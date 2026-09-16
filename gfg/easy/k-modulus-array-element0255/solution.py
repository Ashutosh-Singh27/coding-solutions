import math

class Solution:
    def sameMod(self, arr):
        if all(x == arr[0] for x in arr):
            return -1

        g = 0
        for x in arr:
            g = math.gcd(g, abs(x - arr[0]))

        # count divisors of g
        count = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                count += 1
                if i != g // i:
                    count += 1
            i += 1

        return count