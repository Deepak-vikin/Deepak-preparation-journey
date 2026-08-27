"""
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).



Example 1:


Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.
"""

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        n=len(grid)
        m=len(grid[0])
        dist=[[float("inf")]*m for _ in range(n)]
        dist[0][0]=0
        queue=deque([(0,0)])
        while queue:
            sx,sy=queue.popleft()
            for x,y in directions:
                nx=sx+x
                ny=sy+y
                if 0<=nx<n and 0<=ny<m:
                    if grid[nx][ny]==0:
                        weight=0
                    else:
                        weight=1
                    new_dist=dist[sx][sy]+weight
                    if new_dist<dist[nx][ny]:
                        dist[nx][ny]=new_dist
                        if weight==0:
                            queue.appendleft((nx,ny))
                        else:
                            queue.append((nx,ny))
        return dist[-1][-1]
obj=Solution()
res=obj.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]])
print(res)