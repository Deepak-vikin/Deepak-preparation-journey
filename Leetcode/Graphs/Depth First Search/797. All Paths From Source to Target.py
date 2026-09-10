"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).



Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        res=[]
        def dfs(node,path):
            if node in path:
                return
            if node==(n-1):
                path.append(node)
                res.append(path.copy())
                path.pop()
                return
            path.append(node)
            for neigh in graph[node]:
                dfs(neigh,path)
            path.pop()
            return
        dfs(0,[])
        return res
obj=Solution()
res=obj.allPathsSourceTarget([[1,2],[3],[3],[]])
print(res)