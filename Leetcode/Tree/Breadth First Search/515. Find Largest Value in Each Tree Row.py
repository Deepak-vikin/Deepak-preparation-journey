"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque([root])
        res=[]
        if not root:
            return []
        while queue:
            m=-1*float('inf')
            size=len(queue)
            for _ in range(size):
                curr=queue.popleft()
                m=max(m,curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(m)
        return res
obj=Solution()
res=obj.largestValues([1,2,3,4,5,6])
print(res)