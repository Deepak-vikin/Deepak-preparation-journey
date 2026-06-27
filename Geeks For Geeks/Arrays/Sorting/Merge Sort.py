"""
Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: We get the sorted array after using merge sort
"""


class Solution:

    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        self.merge(arr, l, r, mid)

    def merge(self, arr, l, r, mid):
        i = l
        j = mid + 1
        temp = []
        while i <= mid and j <= r:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= r:
            temp.append(arr[j])
            j += 1
        arr[l:r + 1] = temp
        return arr
obj=Solution()
res=obj.mergeSort([1,2,3,4,5,6,7,8,9])
print(res)

