"""
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.
"""


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set([])
        count = 0
        graph = {}
        for u, v in edges:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        count = 0
        for i in range(n):
            if i in visited:
                continue
            component = set([i])
            queue = deque([i])
            edges = 0
            node_c = 0
            while queue:
                curr = queue.popleft()
                node_c += 1
                edges += len(graph.get(curr, []))
                for neigh in graph.get(curr, []):
                    if neigh not in component:
                        queue.append(neigh)
                        component.add(neigh)
            edges //= 2
            visited.update(component)
            if ((node_c * (node_c - 1)) / 2) == edges:
                count += 1
        return count
obj=Solution()
res=obj.countCompleteComponents(6,[[0,1],[0,2],[1,2],[3,4]])
print(res)


