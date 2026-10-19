"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        f=0
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                f=1
                return mid
            elif target < nums[mid]:
                high=mid-1
            elif target>nums[mid]:
                low=mid+1
        if f==0:
            pos=0
            for i in range(len(nums)):
                if nums[i] > target:
                    pos=i
                    break
            else:
                pos=len(nums)
            nums.insert(pos-1,target)
            return pos
obj=Solution()
nums=[1,3,5,6]
target=5
print(obj.searchInsert(nums,target))