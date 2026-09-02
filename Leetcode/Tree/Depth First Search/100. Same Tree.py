"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root,res):
            if not root:
                res.append(None)
                return res
            res.append(root.val)
            dfs(root.left,res)
            dfs(root.right,res)
            return res
        tree1=dfs(p,[])
        tree2=dfs(q,[])
        if tree1==tree2:
            return True
        return False
obj=Solution()
res=obj.isSameTree([1,2,3],[1,2,3])
print(res)