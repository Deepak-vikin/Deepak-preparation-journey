"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        mdepth=float('inf')
        if not root:
            return 0
        depth=1
        while queue:
            size=len(queue)
            for _ in range(size):
                curr=queue.popleft()
                if not curr.left and not curr.right:
                    mdepth=min(mdepth,depth)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            depth+=1
        return mdepth
obj=Solution()
res=obj.minDepth([3,9,20,null,null,15,7])
print(res)