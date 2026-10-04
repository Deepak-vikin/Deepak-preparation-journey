"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0


Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
"""
class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        hash1={}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                s=nums1[i]+nums2[j]
                hash1[s]=hash1.get(s,0)+1
        count=0
        for c in nums3:
            for d in nums4:
                s=c+d
                if -s in hash1:
                    count+=hash1[-s]
        return count
obj=Solution()
res=obj.fourSumCount([1,2],[-2.-1],[-1,2],[0,2])
print(res)