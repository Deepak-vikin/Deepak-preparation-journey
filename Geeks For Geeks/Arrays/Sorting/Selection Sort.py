"""
class Solution:
    def selectionSort(self, arr):
        n=len(arr)
        for i in range(n-1):
            m=i
            for j in range(i,n):
                if arr[j]<arr[m]:
                    m=j
            temp=arr[i]
            arr[i]=arr[m]
            arr[m]=temp
        return arr
"""
class Solution:
    def selectionSort(self, arr):
        n=len(arr)
        for i in range(n-1):
            m=i
            for j in range(i,n):
                if arr[j]<arr[m]:
                    m=j
            temp=arr[i]
            arr[i]=arr[m]
            arr[m]=temp
        return arr
obj = Solution()
res=obj.selectionSort([64, 25, 12, 22, 11])
print(res)