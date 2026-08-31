"""
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.



Example 1:


Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]"""
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n=len(graph)
        target=(1<<n)-1
        visited=set()
        queue=deque([])
        for i in range(n):
            mask=1<<i
            visited.add((i,mask))
            queue.append((i,mask,0))
        while queue:
            curr,m,dist=queue.popleft()
            if m==target:
                return dist
            for neigh in graph[curr]:
                new=m|(1<<neigh)
                if (neigh,new) not in visited:
                    queue.append((neigh,new,dist+1))
                    visited.add((neigh,new))
obj=Solution()
graph=[[1,2,3],[0],[0],[0]]
res=obj.shortestPathLength(graph)