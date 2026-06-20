class Solution:
    def sortColors(self, nums: List[int]) -> None:
        res=[]
        for i in range(3):
            for j in nums:
                if i==j:
                    res.append(j)
        nums[:]=res
obj=Solution()
res=obj.sortColors([2,0,2,1,1,0])
print(res)