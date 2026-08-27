"""
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.



Example 1:


Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
"""
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        n=len(board)
        m=len(board[0])
        state=""
        for i in range(n):
            for j in range(m):
                state+=str(board[i][j])
        visited=set([state])
        queue=deque([state])
        steps=0
        neighbors = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
        }
        while queue:
            for _ in range(len(queue)):
                curr=queue.popleft()
                arr=list(curr)
                if curr=="123450":
                    return steps
                for i in range(len(arr)):
                    if arr[i]=="0":
                        for x in neighbors.get(i,[]):
                            arr[i],arr[x]=arr[x],arr[i]
                            new_state="".join(arr)
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append(new_state)
                            arr[i],arr[x]=arr[x],arr[i]
            steps+=1
        return -1
obj=Solution()
res=obj.slidingPuzzle([[1,2,3],[4,0,5]])
print(res)
