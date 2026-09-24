"""
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.

Example 1:

Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
Output: 4
Explanation: The diagram above shows the tree.
We have that [0,1,2,3] are the only nodes that can be reached from node 0 without visiting a restricted node.
"""
class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        graph={}
        restricted=set(restricted)
        for u,v in edges:
            if u not in restricted and v not in restricted:
                graph.setdefault(u,[]).append(v)
                graph.setdefault(v,[]).append(u)
        visited=set([0])
        queue=deque([0])
        count=0
        while queue:
            curr=queue.popleft()
            count+=1
            for neigh in graph.get(curr,[]):
                if neigh not in visited:
                    queue.append(neigh)
                    visited.add(neigh)
        return count
obj=Solution()
res=obj.reachableNodes(7,[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]],[4,5])
print(res)