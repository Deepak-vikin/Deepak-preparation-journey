"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.



Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation:
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set([])
        n=len(rooms)
        count=0
        def dfs(node):
            nonlocal count
            visited.add(node)
            count+=1
            if count==n:
                return True
            for neigh in rooms[node]:
                if neigh not in visited:
                    if dfs(neigh):
                        return True
            return False
        return dfs(0)
obj=Solution()
res=obj.canVisitAllRooms([[1],[2],[3],[]])
print(res)