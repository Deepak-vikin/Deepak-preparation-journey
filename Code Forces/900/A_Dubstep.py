s=input()
i=0
ans=[]
st=""
while i<len(s):
    if s[i:i+3]=="WUB":
        if st:
            ans.append(st)
        st=""
        i=i+3
    else:
        st+=s[i]
        i+=1
if st:
    ans.append(st)
print(" ".join(ans))
