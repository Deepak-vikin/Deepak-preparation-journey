"""
You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

'S': Starting position of the student
'L': Litter that must be collected (once collected, the cell becomes empty)
'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
'X': Obstacle the student cannot pass through
'.': Empty space
You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.



Example 1:

Input: classroom = ["S.", "XL"], energy = 2

Output: 2

Explanation:

The student starts at cell (0, 0) with 2 units of energy.
Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
A valid sequence of moves to collect all litter is as follows:
Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
The student collects all the litter using 2 moves. Thus, the output is 2.
"""
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        m=len(classroom)
        n=len(classroom[0])
        queue=deque([])
        visited=set([])
        lcount=0
        aenergy=energy
        litter={}
        sr=sc=0
        for i in range(m):
            for j in range(n):
                if classroom[i][j]=="S":
                    sr=i
                    sc=j
                if classroom[i][j]=="L":
                    litter[(i,j)]=lcount
                    lcount+=1
        mask=(1<<lcount)-1
        queue.append((sr,sc,energy,0,0))
        visited.add((sr,sc,energy,0))
        if mask==0:
            return 0
        while queue:
            sx,sy,energy,curr_mask,moves=queue.popleft()
            if curr_mask==mask:
                return moves
            for x,y in directions:
                nx=sx+x
                ny=sy+y
                if 0<=nx<m and 0<=ny<n and classroom[nx][ny]!="X":
                    new_energy=energy-1
                    if new_energy<0:
                        continue
                    new_mask=curr_mask
                    if classroom[nx][ny]=="R":
                        new_energy=aenergy
                    if classroom[nx][ny]=="L":
                        index=litter[(nx,ny)]
                        new_mask=curr_mask|(1<<index)
                    if (nx,ny,new_energy,new_mask) not in visited:
                        visited.add((nx,ny,new_energy,new_mask))
                        queue.append((nx,ny,new_energy,new_mask,moves+1))
        return -1
obj=Solution()
res=obj.minMoves(["LS", "RL"])
print(res)
