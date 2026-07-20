"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
In one shift operation:
Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
"""

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        v=[]
        for i in grid:
            v.append(i[:])
        for _ in range(k):
            for i in range(m):
                for j in range(n):
                    if j+1<n:
                        v[i][j+1]=grid[i][j]
                    if i+1<m:
                        v[i+1][0]=grid[i][n-1]
            v[0][0]=grid[m-1][n-1]
            grid=[]
            for x in v:
                grid.append(x[:])
        return v
obj=Solution()
res=obj.shiftGrid([[1,2,3],[4,5,6],[7,8,9]],1)
print(res)