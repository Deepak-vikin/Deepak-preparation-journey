"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count=0
        n=len(isConnected)
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        visited=set()
        graph={}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    graph.setdefault(i,[]).append(j)
        for x in range(n):
            if x not in visited:
                queue=deque([x])
                visited.add(x)
                while queue:
                    curr=queue.popleft()
                    for neigh in graph.get(curr,[]):
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append(neigh)
                count+=1
        return count
obj=Solution()
res=obj.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
print(res)

