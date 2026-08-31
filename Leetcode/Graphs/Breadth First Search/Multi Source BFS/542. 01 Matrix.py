"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.



Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        solution=[[float("inf")]*m for _ in range(n)]
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        queue=deque([])
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    solution[i][j]=0
                    queue.append((i,j))
        while queue:
            sx,sy=queue.popleft()
            for x,y in directions:
                nx=sx+x
                ny=sy+y
                if 0<=nx<n and 0<=ny<m:
                    new_dist=solution[sx][sy]+1
                    if new_dist<solution[nx][ny]:
                        solution[nx][ny]=new_dist
                        queue.append((nx,ny))
        return solution
obj=Solution()
res=obj.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
print(res)
