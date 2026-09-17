"""
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.



Example 1:


Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.
"""
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        ans=-1
        graph={}
        for i,v in enumerate(edges):
            if v!=-1:
                graph.setdefault(i,[]).append(v)
        global_visited=set([])
        for i in range(n):
            queue=deque([(i,0)])
            visited={i:0}
            if i in global_visited:
                continue
            while queue:
                curr,d=queue.popleft()
                global_visited.add(curr)
                for neigh in graph.get(curr,[]):
                    if neigh not in visited:
                        if neigh in global_visited:
                            break
                        visited[neigh]=d+1
                        queue.append((neigh,d+1))
                    else:
                        l=d+1-visited[neigh]
                        ans=max(ans,l)
                        break
        return ans
obj=Solution()
res=obj.longestCycle([3,3,4,2,3])
print(res)