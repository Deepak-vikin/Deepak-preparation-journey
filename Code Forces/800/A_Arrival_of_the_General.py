n=int(input())
nums=list(map(int,input().split()))
min_num=min(nums)
min_index=0
for i in range(n):
    if nums[i]==min_num:
        min_index=i
max_num=max(nums)
max_index=0
for i in range(n):
    if nums[i]==max_num:
        max_index=i
        break
ans=(n-min_index-1)+max_index
if min_index<max_index:
    ans-=1
print(ans)