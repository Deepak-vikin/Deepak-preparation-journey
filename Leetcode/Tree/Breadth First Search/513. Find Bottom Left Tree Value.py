"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.



Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        ans=0
        while queue:
            size=len(queue)
            for _ in range(size):
                curr=queue.popleft()
                if _ == 0:
                    ans=curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return ans
obj=Solution()
res=obj.findBottomLeftValue([2,1,3])
print(res)