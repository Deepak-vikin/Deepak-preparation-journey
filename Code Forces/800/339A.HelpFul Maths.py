s=input()
lst=s.split("+")
lst.sort()
ans=""
for i in range(len(lst)-1):
    ans+=lst[i]
    ans+="+"
ans+=lst[-1]
print(ans)
