"""
Implement Quick Sort, a Divide and Conquer algorithm, to sort an array, arr[] in ascending order.
Given an array arr[], with starting index low and ending index high, complete the functions partition() and quickSort().
Use the last element as the pivot, so that all elements less than or equal to the pivot come before it, and elements greater than the pivot follow it.

Note: low and high are inclusive.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: After sorting, all elements are arranged in ascending order.
"""


class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p - 1)
            self.quickSort(arr, p + 1, high)

    def partition(self, arr, low, high):
        piv = arr[low]
        i = low + 1
        j = high
        while i <= j:
            while i <= high and arr[i] <= piv:
                i += 1
            while j >= low and arr[j] > piv:
                j -= 1
            if i < j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        temp = arr[low]
        arr[low] = arr[j]
        arr[j] = temp
        return j
obj = Solution()
res=obj.quickSort([4,1,3,9,7])
print(res)