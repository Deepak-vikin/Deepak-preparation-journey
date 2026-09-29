t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    if nums.count(1)>=nums.count(0):
        print("Bessie")
    else:
        print("Elsie")