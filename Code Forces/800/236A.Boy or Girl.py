n=input()
freq={}
for i in n:
    freq[i]=freq.get(i,0)+1
count=0
if len(freq)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
