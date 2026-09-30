n=int(input())
if n<26:
    print("NO")
else:
    s=input().lower()
    chars=[0]*26
    for ch in s:
        chars[ord(ch)-ord("a")]+=1
    if any(i==0 for i in chars):
        print("NO")
    else:
        print("YES")