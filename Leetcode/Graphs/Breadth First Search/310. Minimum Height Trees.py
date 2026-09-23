"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n==1:
            return [0]
        graph={}
        for u,v in edges:
            graph.setdefault(u,[]).append(v)
            graph.setdefault(v,[]).append(u)
        degree=[0]*n
        for i in range(n):
            degree[i]=len(graph.get(i,[]))
        queue=deque()
        for i in range(n):
            if degree[i]==1:
                queue.append(i)
        remaining=n
        while remaining>2:
            size=len(queue)
            remaining-=size
            for _ in range(size):
                curr=queue.popleft()
                for neigh in graph.get(curr,[]):
                    degree[neigh]-=1
                    if degree[neigh]==1:
                        queue.append(neigh)
        return list(queue)
obj=Solution()
res=obj.findMinHeightTrees(4,[[1,0],[1,2],[1,3]])
print(res)