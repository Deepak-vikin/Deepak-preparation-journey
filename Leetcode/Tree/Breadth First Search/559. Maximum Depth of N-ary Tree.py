"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: 3
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue=deque([root])
        depth=0
        if not root:
            return 0
        while queue:
            size=len(queue)
            for _ in range(size):
                curr=queue.popleft()
                for child in curr.children:
                    queue.append(child)
            depth+=1
        return depth
obj=Solution()
res=obj.maxDepth([1,null,3,2,4,null,5,6])
print(res)

