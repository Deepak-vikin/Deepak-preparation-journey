"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
"""
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def binary_search(target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    return mid
                elif target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            return left
        return binary_search(target)
obj=Solution()
nums=[1,3,5,6]
target=5
print(obj.searchInsert(nums,target))