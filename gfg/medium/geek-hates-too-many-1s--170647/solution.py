class Solution:
    def maxValue(self, n: int) -> int:
        bits = list(bin(n)[2:])
        count = 0
        for i in range(len(bits)):
            if bits[i] == '1':
                count += 1
                if count == 3:
                    bits[i] = '0'
                    count = 0
            else:
                count = 0
        return int(''.join(bits), 2)