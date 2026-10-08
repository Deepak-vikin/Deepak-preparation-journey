"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
"""
def rob2(self, nums: List[int]) -> int:
    n=len(nums)
    prev1=0
    prev2=nums[0]
    for i in range(1,n):
        sum1=prev1+nums[i]
        sum2=prev2
        curr=max(sum1,sum2)
        prev1=prev2
        prev2=curr
    return prev2
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        temp1=[]
        temp2=[]
        for i in range(len(nums)):
            if i!=0:
                temp1.append(nums[i])
            if i!=n-1:
                temp2.append(nums[i])
        return max(rob2(self,temp1),rob2(self,temp2))
obj=Solution()
res=obj.rob([2,3,2])
print(res)