n=int(input())
d={}
for _ in range(n):
    s=input()
    if s not in d:
        d[s]=1
        print("OK")
    else:
        print(s+str(d[s]))
        d[s]+=1
    