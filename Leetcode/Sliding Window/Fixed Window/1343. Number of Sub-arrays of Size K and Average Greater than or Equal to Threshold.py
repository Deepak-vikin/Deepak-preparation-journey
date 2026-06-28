"""
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.



Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
"""

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=0
        a=0
        c=0
        for i in range(k):
            s+=arr[i]
        a=s/k
        if a>=threshold:
            c+=1
        for i in range(k,len(arr)):
            s+=arr[i]
            s-=arr[i-k]
            a=s/k
            if a>=threshold:
                c+=1
        return c
obj=Solution()
res=obj.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4)
print(res)