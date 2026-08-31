"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        if not root:
            return []
        res=[]
        while queue:
            ls=[]
            for _ in range(len(queue)):
                curr=queue.popleft()
                ls.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(ls)
        return res[::-1]
obj=Solution()
print(obj.levelOrderBottom(None))
print(obj.levelOrderBottom([3,9,20,null,null,15,7]))
print(obj.levelOrderBottom([1]))