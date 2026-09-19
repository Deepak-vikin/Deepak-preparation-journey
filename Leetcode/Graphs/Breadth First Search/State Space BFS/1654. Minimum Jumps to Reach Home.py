"""
A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.



Example 1:

Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
"""
class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        queue=deque([(0,False)])
        visited=set([(0,False)])
        steps=0
        forbidden=set(forbidden)
        limit=max(max(forbidden),x)+a+b
        while queue:
            size=len(queue)
            for _ in range(size):
                curr_pos,last_backward=queue.popleft()
                if curr_pos==x:
                    return steps
                next_pos=curr_pos+a
                if next_pos not in forbidden and (next_pos,False) not in visited and next_pos<=limit:
                    queue.append((next_pos,False))
                    visited.add((next_pos,False))
                if not last_backward:
                    next_pos=curr_pos-b
                    if next_pos not in forbidden and (next_pos,True) not in visited and next_pos>=0:
                        queue.append((next_pos,True))
                        visited.add((next_pos,True))
            steps+=1
        return -1
obj=Solution()
res=obj.minimumJumps([14,4,18,1,15],3,15,9)
print(res)