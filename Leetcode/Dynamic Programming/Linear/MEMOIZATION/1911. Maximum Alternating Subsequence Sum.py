"""
The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.

Example 1:

Input: nums = [4,2,5,3]
Output: 7
Explanation: It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.

"""
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        def func(num,prev):
            if num<0:
                return 0
            if dp[num][prev]!=-1:
                return dp[num][prev]
            if prev==1:
                s1=nums[num]+func(num-1,0)
            else:
                s1=-nums[num]+func(num-1,1)
            s2=func(num-1,prev)
            dp[num][prev]=max(s1,s2)
            return dp[num][prev]
        n=len(nums)
        dp=[[-1]*2 for _ in range(n)]
        return func(n-1,1)
res=Solution().maxAlternatingSum([4,2,5,3])
print(res)