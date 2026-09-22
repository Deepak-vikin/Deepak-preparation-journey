"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.



Example 1:

Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
"""


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        terminal = set([])
        n = len(graph)
        g = {}
        outdegree = {i: 0 for i in range(n)}
        for num in range(len(graph)):
            for x in graph[num]:
                g.setdefault(x, []).append(num)
                outdegree[num] += 1
        queue = deque([])
        visited = set([])
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)
                visited.add(i)
                res.append(i)
        while queue:
            curr = queue.popleft()
            for neigh in g.get(curr, []):
                outdegree[neigh] -= 1
                if outdegree[neigh] == 0:
                    queue.append(neigh)
                    visited.add(neigh)
                    res.append(neigh)
        return sorted(res)
obj=Solution()
res=obj.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])
print(res)



