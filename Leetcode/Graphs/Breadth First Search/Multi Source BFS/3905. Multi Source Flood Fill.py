"""
You are given two integers n and m representing the number of rows and columns of a grid, respectively.

You are also given a 2D integer array sources, where sources[i] = [ri, ci, color​​​​​​​i] indicates that the cell (ri, ci) is initially colored with colori. All other cells are initially uncolored and represented as 0.

At each time step, every currently colored cell spreads its color to all adjacent uncolored cells in the four directions: up, down, left, and right. All spreads happen simultaneously.

If multiple colors reach the same uncolored cell at the same time step, the cell takes the color with the maximum value.

The process continues until no more cells can be colored.

Return a 2D integer array representing the final state of the grid, where each cell contains its final color.



Example 1:

Input: n = 3, m = 3, sources = [[0,0,1],[2,2,2]]

Output: [[1,1,2],[1,2,2],[2,2,2]]

Explanation:
At time step 2, cells (0, 2), (1, 1), and (2, 0) are reached by both colors, so they are assigned color 2 as it has the maximum value among them.
"""
class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        graph=[[0]*m for _ in range(n)]
        sources.sort(key=lambda x:-x[2])
        queue=deque([])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        for x,y,colour in sources:
            graph[x][y]=colour
        for x,y,colour in sources:
            queue.append((x,y,colour))
        while queue:
            sx,sy,colour=queue.popleft()
            for x,y in directions:
                nx=sx+x
                ny=sy+y
                if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                    graph[nx][ny]=colour
                    queue.append((nx,ny,colour))
        return graph

obj=Solution()
res=obj.colorGrid(n=3,m=3,sources=[[1,1,1],[1,1,1],[1,1,1]])
print(res)
