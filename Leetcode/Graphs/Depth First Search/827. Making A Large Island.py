"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.



Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
"""
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        comp=[[-1]*m for _ in range(n)]
        counts=[]
        def dfs(x,y,id):
            stack=[(x,y)]
            comp[x][y]=id
            count=0
            while stack:
                sx,sy=stack.pop()
                count+=1
                for dx,dy in directions:
                    nx=sx+dx
                    ny=sy+dy
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]!=0 and comp[nx][ny]==-1:
                        comp[nx][ny]=id
                        stack.append((nx,ny))
            return count
        id=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0 and comp[i][j]==-1:
                    count=dfs(i,j,id)
                    id+=1
                    counts.append(count)
        ans=max(counts,default=0)
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    continue
                seen=set()
                curr=1
                for x,y in directions:
                    nx=i+x
                    ny=j+y
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1:
                        id=comp[nx][ny]
                        if id not in seen:
                            seen.add(id)
                            curr+=counts[id]
                ans=max(ans,curr)
        return ans
obj=Solution()
res =obj.largestIsland([[1,0],[0,1]])
print(res)