class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            s=numbers[l]+numbers[r]
            if s<target:
                l+=1
            elif s>target:
                r-=1
            else:
                return [l+1,r+1]
obj=Solution()
res=obj.twoSum([-1,0,1,2], 1)
print(res)