"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:
Input: root = [1,2]
Output: 1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        if not root:
            return 0
        def level_order_traversal(root):
            queue=deque([root])
            level=0
            while queue:
                size=len(queue)
                for _ in range(size):
                    curr=queue.popleft()
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level+=1
            return level
        ans=0
        while queue:
            size=len(queue)
            leftlevels=rightlevels=0
            for _ in range(size):
                curr=queue.popleft()
                if curr.left:
                    leftlevels=level_order_traversal(curr.left)
                    queue.append(curr.left)
                if curr.right:
                    rightlevels=level_order_traversal(curr.right)
                    queue.append(curr.right)
                ans=max(ans,leftlevels+rightlevels)
        return ans
obj=Solution()
res=obj.diameterOfBinaryTree([1,2,3,4,5])
print(res)
