"""
You are given two jugs with capacities x liters and y liters. You have an infinite water supply. Return whether the total amount of water in both jugs may reach target using the following operations:

Fill either jug completely with water.
Completely empty either jug.
Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty.


Example 1:

Input: x = 3, y = 5, target = 4

Output: true

Explanation:

Follow these steps to reach a total of 4 liters:

Fill the 5-liter jug (0, 5).
Pour from the 5-liter jug into the 3-liter jug, leaving 2 liters (3, 2).
Empty the 3-liter jug (0, 2).
Transfer the 2 liters from the 5-liter jug to the 3-liter jug (2, 0).
Fill the 5-liter jug again (2, 5).
Pour from the 5-liter jug into the 3-liter jug until the 3-liter jug is full. This leaves 4 liters in the 5-liter jug (3, 4).
Empty the 3-liter jug. Now, you have exactly 4 liters in the 5-liter jug (0, 4).
"""
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        queue=deque([(0,0)])
        visited=set([])
        while queue:
            a,b=queue.popleft()
            if a+b==target:
                return True
            states=[(x,b),(a,y),(0,b),(a,0)]
            pour=min(a,y-b)
            states.append((a-pour,b+pour))
            pour=min(b,x-a)
            states.append((a+pour,b-pour))
            for l,k in states:
                if (l,k) not in visited:
                    queue.append((l,k))
                    visited.add((l,k))
        return False
obj=Solution()
res=obj.canMeasureWater(3,5,4)
print(res)