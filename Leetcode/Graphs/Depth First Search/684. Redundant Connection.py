"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph={}
        def dfs(node1,node2,visited):
            if node1==node2:
                return True
            visited.add(node1)
            for neigh in graph.get(node1,[]):
                if neigh not in visited:
                    if dfs(neigh,node2,visited):
                        return True
            return False
        for num in edges:
            u,v=num
            visited=set([])
            if dfs(u,v,visited):
                return [u,v]
            graph.setdefault(u,[]).append(v)
            graph.setdefault(v,[]).append(u)
obj=Solution()
res=obj.findRedundantConnection([[1,2],[1,3],[2,3]])
print(res)