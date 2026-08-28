"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue=deque([(root,root.val)])
        while queue:
            curr,s=queue.popleft()
            if s==targetSum and not curr.left and not curr.right:
                return True
            if curr.left:
                queue.append((curr.left,s+curr.left.val))
            if curr.right:
                queue.append((curr.right,s+curr.right.val))
        return False
obj=Solution()
res=obj.hasPathSum(root=None,targetSum=0)
print(res)