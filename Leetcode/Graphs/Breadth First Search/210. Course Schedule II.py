"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        n=numCourses
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
            res.append(curr)
            for neigh in graph.get(curr,[]):
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        return res if len(res)==n else []
obj=Solution()
res=obj.findOrder(numCourses=2, prerequisites=[[1,0],[0,1]])
print(res)