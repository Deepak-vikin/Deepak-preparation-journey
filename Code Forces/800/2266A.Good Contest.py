t=int(input())
for _ in range(t):
  n=int(input())
  lst=list(map(int,input().split()))
  print(n-min(lst))