"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.



Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph={}
        for u,v,c in flights:
            graph.setdefault(u,[]).append((v,c))
        heap=[(0,src,1)]
        visited=set([()])
        k=k+2
        while heap:
            cost,node,n_count=heappop(heap)
            if n_count>k:
                continue
            if (node,n_count) in visited:
                continue
            visited.add((node,n_count))
            if node==dst:
                return cost
            for next,c in graph.get(node,[]):
                next_cost=cost+c
                if n_count+1>k:
                    continue
                heappush(heap,(next_cost,next,n_count+1))
        return -1
obj=Solution()
res=obj.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1)
print(res)