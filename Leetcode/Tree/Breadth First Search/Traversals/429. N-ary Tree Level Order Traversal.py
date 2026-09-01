"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue=deque([root])
        res=[]
        if not root:
            return []
        while queue:
            ls=[]
            size=len(queue)
            for _ in range(size):
                curr=queue.popleft()
                ls.append(curr.val)
                for child in curr.children:
                    queue.append(child)
            res.append(ls)
        return res
obj=Solution()
res=obj.levelOrder(None)
print(res)