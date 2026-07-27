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
        def bfs(tree1,tree2):
            queue=deque([(tree1,tree2)])
            while queue:
                n1,n2=queue.popleft()
                if not n1 and not n2:
                    continue
                if not n1 or not n2:
                    return False
                if n1.val!=n2.val:
                    return False
                queue.append((n1.left,n2.left))
                queue.append((n1.right,n2.right))
            return True
        return bfs(p,q)
obj=Solution()
res=obj.isSameTree(p = [1,2,3], q = [1,2,3])
print(res)