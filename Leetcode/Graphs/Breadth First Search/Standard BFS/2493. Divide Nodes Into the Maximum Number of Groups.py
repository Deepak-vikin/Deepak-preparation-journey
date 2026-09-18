"""
You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.



Example 1:


Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4
Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.
"""
class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        graph={}
        for u,v in edges:
            graph.setdefault(u,[]).append(v)
            graph.setdefault(v,[]).append(u)
        queue=deque([1])
        map={}
        grp=1
        def is_bipartide(graph):
            map={}
            for i in range(n):
                if i in map:
                    continue
                map[i]=1
                queue=deque([i])
                while queue:
                    curr=queue.popleft()
                    for neigh in graph.get(curr,[]):
                        if neigh not in map:
                            if map[curr]==1:
                                map[neigh]=2
                            else:
                                map[neigh]=1
                            queue.append(neigh)
                        elif map[neigh]==map[curr]:
                            return False
            return True
        if not is_bipartide(graph):
            return -1
        global_set=set([])
        ans=0
        for j in range(1,n+1):
            if j in global_set:
                continue
            visited=set([j])
            queue=deque([j])
            while queue:
                size=len(queue)
                for _ in range(size):
                    curr=queue.popleft()
                    for neigh in graph.get(curr,[]):
                        if neigh not in visited:
                            queue.append(neigh)
                            visited.add(neigh)
            curr_ans=0
            global_set.update(visited)
            for i in visited:
                levels=0
                queue=deque([i])
                v=set([i])
                while queue:
                    size=len(queue)
                    for _ in range(size):
                        curr=queue.popleft()
                        for neigh in graph.get(curr,[]):
                            if neigh not in v:
                                queue.append(neigh)
                                v.add(neigh)
                    levels+=1
                curr_ans=max(curr_ans,levels)
            ans+=curr_ans
        return ans
obj=Solution()
res=obj.magnificentSets(6,[[1,2],[1,4],[1,5]])
print(res)
