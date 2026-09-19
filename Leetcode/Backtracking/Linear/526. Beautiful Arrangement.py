"""
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        perm=[]
        arr=[i for i in range(1,n+1)]
        used=[0]*len(arr)
        count=0
        def dfs(i,path):
            nonlocal count
            if i==len(arr):
                count+=1
                return
            for j in range(len(arr)):
                if used[j]:
                    continue
                pos=i+1
                num=arr[j]
                if pos%num!=0 and num%pos!=0:
                    continue
                used[j]=1
                dfs(i+1,path+[arr[j]])
                used[j]=0
        dfs(0,[])
        return count
obj=Solution()
print(obj.countArrangement(7))

