"""
You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.



Example 1:

Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

Output: [8,4,6,5,6]

Explanation:

Operation	Result
After operation 1	[2, 2, 3, 5, 6]
After operation 2	[4, 2, 3, 5, 6]
After operation 3	[4, 4, 3, 5, 6]
After operation 4	[4, 4, 6, 5, 6]
After operation 5	[8, 4, 6, 5, 6]

"""
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr=[]
        for i,v in enumerate(nums):
            heappush(arr,(v,i))
        for i in range(k):
            min_elem,idx=heappop(arr)
            new_num=min_elem*multiplier
            heappush(arr,(new_num,idx))
        res=[0]*len(nums)
        for i in arr:
            res[i[1]]=i[0]
        return res
obj=Solution()
res=obj.getFinalState(nums=[2,1,3,5,6],k=5,multiplier=2)
print(res)