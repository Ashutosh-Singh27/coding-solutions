arr = tuple(map(int, input().split()))

# code here
if len(set(arr))==len(arr):
    print("True")
else:
    print("False")