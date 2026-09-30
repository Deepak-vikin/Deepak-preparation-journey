name=input()
host=input()
target=input()
chars=[0]*26
for ch in name:
    chars[ord(ch)-ord('A')]+=1
for ch in host:
    chars[ord(ch)-ord('A')]+=1
res=[0]*26
for ch in target:
    res[ord(ch)-ord("A")]+=1
if chars==res:
    print("YES")
else:
    print("NO")
    