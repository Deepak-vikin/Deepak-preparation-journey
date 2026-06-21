class Solution:
    def check(self, nums: List[int]) -> bool:
        s=sorted(nums)
        m=sorted(nums)
        n=len(nums)
        for i in range(n):
            r1=s[i:]+s[:i]
            r2=m[:i] + m[i:]
            if r1==nums or r2==nums:
                return True
        return False
obj=Solution()
res=obj.check([3,4,5,1,2])
print(res)