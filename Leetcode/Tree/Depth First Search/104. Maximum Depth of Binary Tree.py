"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node,depth):
            if not node:
                return depth
            left=dfs(node.left,depth+1)
            right=dfs(node.right,depth+1)
            return max(left,right)
        return dfs(root,0)
obj=Solution()
res=obj.maxDepth([3,9,20,null,null,15,7])
print(res)