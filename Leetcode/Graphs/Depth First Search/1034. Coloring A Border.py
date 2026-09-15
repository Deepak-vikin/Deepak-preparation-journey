"""
You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

Two squares are called adjacent if they are next to each other in any of the 4 directions.

Two squares belong to the same connected component if they have the same color and they are adjacent.

The border of a connected component is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).

You should color the border of the connected component that contains the square grid[row][col] with color.

Return the final grid.



Example 1:

Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
Output: [[3,3],[3,2]]
"""
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        n=len(grid)
        m=len(grid[0])
        visited=set([])
        def dfs(x,y):
            if x<0 or y<0 or x>=n or y>=m:
                return
            visited.add((x,y))
            for sx,sy in directions:
                nx=sx+x
                ny=sy+y
                if (x==0 or x==n-1 or y==0 or y==m-1 ) or (grid[nx][ny]!=curr_color and (nx,ny) not in visited):
                    grid[x][y]=color
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]==curr_color and (nx,ny) not in visited:
                    dfs(nx,ny)
        curr_color=grid[row][col]
        dfs(row,col)
        return grid
obj=Solution()
res=obj.colorBorder([[1,1],[1,2]],1,3)
print(res)
