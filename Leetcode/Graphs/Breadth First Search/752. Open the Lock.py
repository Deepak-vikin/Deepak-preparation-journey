"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.



Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        steps = 0
        start = "0000"
        dead = set(deadends)
        if start in dead:
            return -1
        queue = deque([start])
        visited = set([start])
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return steps
                for i in range(4):
                    state = int(curr[i])
                    s1 = (state + 1) % 10
                    next_state1 = curr[:i] + str(s1) + curr[i + 1:]
                    if next_state1 not in dead and next_state1 not in visited:
                        queue.append(next_state1)
                        visited.add(next_state1)
                    s2 = (state - 1) % 10
                    next_state2 = curr[:i] + str(s2) + curr[i + 1:]
                    if next_state2 not in dead and next_state2 not in visited:
                        queue.append(next_state2)
                        visited.add(next_state2)
            steps += 1
        return -1
obj=Solution()
res=obj.openLock(["0201","0101","0102","1212","2002"])
print(res)
