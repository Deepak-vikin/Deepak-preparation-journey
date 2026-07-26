"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        if not root:
            return []
        res=[]
        level=0
        while queue:
            size=len(queue)
            lst=[]
            for _ in range(size):
                curr=queue.popleft()
                lst.append(curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            if level%2==0:
                lst.reverse()
            level+=1
            res.append(lst)
        return res
obj=Solution()
res=obj.zigzagLevelOrder([1,2,3,4,null,null,5])
print(res)