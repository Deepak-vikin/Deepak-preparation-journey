"""
There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

Each time you pass through a city, you must pay a passing fee. This is represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay when you pass through city j.

In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the summation of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).

Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it within maxTime minutes.


Example 1:

Input: maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Output: 11
Explanation: The path to take is 0 -> 1 -> 2 -> 5, which takes 30 minutes and has $11 worth of passing fees.
"""
class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        graph={}
        n=len(passingFees)
        for u,v,t in edges:
            graph.setdefault(u,[]).append((v,t))
            graph.setdefault(v,[]).append((u,t))
        heap=[]
        visited=set([])
        heapq.heappush(heap,(passingFees[0],0,0))
        visited.add((0,0))
        while heap:
            fees,t,node=heappop(heap)
            if t>maxTime:
                continue
            if node==n-1:
                return fees
            for neigh in graph.get(node,[]):
                next_node=neigh[0]
                time=neigh[1]
                new_fee=passingFees[next_node]
                new_time=time+t
                if new_time<=maxTime and (next_node,time+t) not in visited:
                    heappush(heap,(new_fee+fees,time+t,next_node))
                    visited.add((next_node,time+t))
        return -1
obj=Solution()
res=obj.minCost(30,[[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]],[5,1,2,20,20,3])
print(res)