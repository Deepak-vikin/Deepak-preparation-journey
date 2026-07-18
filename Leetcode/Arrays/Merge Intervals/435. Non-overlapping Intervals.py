"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        modif=sorted(intervals)
        count=0
        prev=modif[0][1]
        for i in range(1,len(modif)):
            if prev>modif[i][0]:
                count+=1
                prev=min(prev,modif[i][1])
            else:
                prev=modif[i][1]
        return count
obj=Solution()
res=obj.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
print(res)