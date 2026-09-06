"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=numCourses
        count=0
        graph={}
        indegree={i:0 for i in range(n)}
        for u,v in prerequisites:
            graph.setdefault(v,[]).append(u)
            indegree[u]+=1
        queue=deque([])
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            curr=queue.popleft()
            count+=1
            for neigh in graph.get(curr,[]):
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        return count==n
obj=Solution()
res=obj.canFinish(numCourses=2, prerequisites=[[1,0],[0,1]])
print(res)