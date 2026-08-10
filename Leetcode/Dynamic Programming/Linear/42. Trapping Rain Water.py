"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        lmax=[0]*(len(height))
        rmax=[0]*len(height)
        lmax[0]=height[0]
        rmax[-1]=height[-1]
        for i in range(1,len(height)):
            lmax[i]=max(lmax[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            rmax[i]=max(rmax[i+1],height[i])
        water=0
        for i in range(len(lmax)):
            water+=min(lmax[i],rmax[i])-height[i]
        return water
obj=Solution()
print(obj.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(obj.trap([0,1,0,2,1,0,1,3,2,1,2,1]))