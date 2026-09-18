"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1. The edges in the graph are represented by a given 2D integer array edges, where edges[i] = [ui, vi] denotes an edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

Return the length of the shortest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node, and each edge in the path is used only once.



Example 1:


Input: n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
Output: 3
Explanation: The cycle with the smallest length is : 0 -> 1 -> 2 -> 0
"""


class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        graph = {}
        for u, v in edges:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        global_set = set([])
        ans = float("inf")
        for i in range(n):
            if i in global_set:
                continue
            queue = deque([i])
            visited = set([i])
            curr_l = float("inf")
            while queue:
                curr = queue.popleft()
                for neigh in graph.get(curr, []):
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
            global_set.update(visited)
            for node in visited:
                queue = deque([(node, -1, 1)])
                v = set([node])
                dist = {node: 1}
                while queue:
                    curr, parent, nodes = queue.popleft()
                    for neigh in graph.get(curr, []):
                        if neigh not in v:
                            queue.append((neigh, curr, nodes + 1))
                            dist[neigh] = nodes + 1
                            v.add(neigh)
                        elif neigh != parent:
                            curr_l = min(curr_l, nodes + dist[neigh] - 1)
            ans = min(ans, curr_l)

        return ans if ans != float("inf") else -1
obj=Solution()
res=obj.findShortestCycle(7,[[1,2],[1,4],[1,5]])
print(res)


