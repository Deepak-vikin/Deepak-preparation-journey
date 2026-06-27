"""
Given an array, arr[] of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

Examples:

Input: arr[] = [2, 4, 3, 5, 6]
Output: [2, 3]
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
Input: arr[] = [1, 1, 1]
Output: [-1]
Explanation: Only element is 1 which is smallest, so there is no second smallest element.
"""


class Solution:
    def minAnd2ndMin(self, arr):
        m = float('inf')
        sm = float('inf')
        for i in arr:
            if i < m:
                sm = m
                m = i
            elif i > m and i < sm:
                sm = i
        if sm == float('inf'):
            return [-1]
        return [m, sm]
obj=Solution()
res=obj.minAnd2ndMin([2, 4, 3, 5, 6])
print(res)
