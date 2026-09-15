"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue=deque([start])
        visited=set([start])
        while queue:
            size=len(queue)
            for _ in range(size):
                curr=queue.popleft()
                if arr[curr]==0:
                    return True
                next_state=curr+arr[curr]
                if 0<=next_state<len(arr) and next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
                next_state=curr-arr[curr]
                if 0<=next_state<len(arr) and next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
        return False
obj=Solution()
res=obj.canReach([4,2,3,0,3,1,2],5)
print(res)