"""
Given an array arr[] of positive integers.The task is to complete the insertsort() function which is used to implement Insertion Sort.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: The sorted array will be [1, 3, 4, 7, 9].
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Explanation: The sorted array will be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
"""
class Solution:
    def insertionSort(self, arr):
        n=len(arr)
        for i in range(n):
            j=i
            while j>0 and arr[j-1]>arr[j]:
                temp=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp
                j-=1
        return arr
obj = Solution()
res=obj.insertionSort([4,1,3,9,7])
print(res)
