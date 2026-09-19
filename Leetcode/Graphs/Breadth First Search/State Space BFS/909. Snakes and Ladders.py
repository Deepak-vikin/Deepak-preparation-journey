"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.



Example 1:


Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
"""


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set([(n - 1, 0)])
        queue = deque([(n - 1, 0)])
        steps = 0

        def find_coordinates(num):
            num -= 1
            row = n - 1 - num // n
            col = num % n
            if (n - 1 - row) % 2 == 1:
                col = n - 1 - col
            return (row, col)

        target = find_coordinates(n * n)
        while queue:
            size = len(queue)
            for _ in range(size):
                sx, sy = queue.popleft()
                if (sx, sy) == target:
                    return steps
                for roll in range(1, 7):
                    nx = sx
                    ny = sy
                    for z in range(roll):
                        if (n - 1 - nx) % 2 == 0:
                            ny += 1
                            if ny >= n:
                                nx -= 1
                                ny = n - 1 - (ny - n)
                            if nx < 0:
                                break
                        else:
                            ny -= 1
                            if ny < 0:
                                nx -= 1
                                ny = -ny - 1
                            if nx < 0:
                                break
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] != -1:
                            new_coordinates = find_coordinates(board[nx][ny])
                        else:
                            new_coordinates = (nx, ny)
                        if new_coordinates not in visited:
                            visited.add(new_coordinates)
                            queue.append(new_coordinates)
            steps += 1
        return -1
obj=Solution()
res=obj.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]])
print(res)