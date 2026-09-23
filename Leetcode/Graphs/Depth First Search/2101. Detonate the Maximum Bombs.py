"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.



Example 1:


Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
"""
class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        graph={}
        for edge in range(len(bombs)):
            for j in range(edge+1,len(bombs)):
                x,y,w=bombs[edge]
                sx,sy,sw=bombs[j]
                dist=math.sqrt((x-sx)**2+(y-sy)**2)
                if dist<=w:
                    graph.setdefault(edge,[]).append(j)
                if dist<=sw:
                    graph.setdefault(j,[]).append(edge)
        if graph=={}:
            return 1
        n=len(bombs)
        ans=0
        def dfs(node):
            nonlocal count
            visited.add(node)
            count+=1
            for neigh in graph.get(node,[]):
                if neigh not in visited:
                    dfs(neigh)
        print(graph)
        for i in range(n):
            count=0
            visited=set([])
            dfs(i)
            ans=max(ans,count)
        return ans
obj=Solution()
res=obj.maximumDetonation([[2,1,3],[6,1,4]])
print(res)