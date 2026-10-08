# cook your dish here
n = int(input())
a = list(map(int, input().split()))
even = sum(1 for x in a if x % 2 == 0)
odd = n - even
print("READY FOR BATTLE" if even > odd else "NOT READY")