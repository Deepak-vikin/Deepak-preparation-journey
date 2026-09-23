"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.



Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
"""
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        def window(k):
            left=0
            s=0
            ans=-1
            for right in range(len(nums)):
                s+=nums[right]
                while left<=right and s>k:
                    s-=nums[left]
                    left+=1
                if s==k:
                    ans=max(ans,right-left+1)
            return ans if ans!=float("inf") else -1
        return len(nums)-window(target) if window(target)!=-1 else -1
obj=Solution()
res=obj.minOperations([1,1,4,2,3],5)
print(res)