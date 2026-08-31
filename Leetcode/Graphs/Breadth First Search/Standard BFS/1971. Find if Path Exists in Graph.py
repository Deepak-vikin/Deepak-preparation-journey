"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.



Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph={}
        for edge in edges:
            u=edge[0]
            v=edge[1]
            if u not in graph:
                graph[u]=[v]
            else:
                graph[u].append(v)
            if v not in graph:
                graph[v]=[u]
            else:
                graph[v].append(u)
        queue=deque([source])
        visited=set([source])
        while queue:
            curr=queue.popleft()
            if curr==destination:
                return True
            for elem in graph.get(curr,[]):
                if elem not in visited:
                    visited.add(elem)
                    queue.append(elem)
        return False
obj=Solution()
res=obj.validPath(n=3, edges=[[0,1],[1,2],[2,0]], source=0, destination=2)
print(res)