"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
from typing import List
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        l=[]
        while (i<len(nums1) and j < len(nums2)):
            if nums1[i]==nums2[j] and nums1[i] not in l:
                l.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return l
obj=Solution()
res=obj.intersection(nums1=[1,2,2,1], nums2=[2,2])
print(res)
