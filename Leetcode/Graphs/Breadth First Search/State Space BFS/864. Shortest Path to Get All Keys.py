"""
You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

Example 1:
Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
"""

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n=len(grid)
        m=len(grid[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        key=set()
        sx=sy=kcount=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="@":
                    sx=i
                    sy=j
                if "a"<=grid[i][j]<="f":
                    kcount+=1
        target=(1<<kcount)-1
        queue=deque([(sx,sy,0,0)])
        visited=set([(sx,sy,0)])
        k=0
        while queue:
            sx,sy,mask,dist=queue.popleft()
            if mask==target:
                return dist
            for x,y in directions:
                nx=sx+x
                ny=sy+y
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]!="#":
                    new_mask=mask
                    curr=grid[nx][ny]
                    if "a"<=curr<="f":
                        key=ord(curr)-ord("a")
                        new_mask=mask|(1<<key)
                    elif "A"<=curr<="F":
                        key=ord(curr)-ord("A")
                        if not (mask & (1<<key)):
                            continue
                    state=(nx,ny,new_mask)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nx,ny,new_mask,dist+1))
        return -1
obj=Solution()
res=obj.shortestPathAllKeys(["@.a..","###.#","b.A.B"])
print(res)