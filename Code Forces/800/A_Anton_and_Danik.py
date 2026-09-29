n=int(input())
freq={}
s=input()
for i in s:
    freq[i]=freq.get(i,0)+1
if "D" not in freq:
    print("Anton")
elif "A" not in freq:
    print("Danik")
elif freq["A"]>freq["D"]:
    print("Anton")
elif freq["A"]<freq["D"]:
    print("Danik")
else:
    print("Friendship")