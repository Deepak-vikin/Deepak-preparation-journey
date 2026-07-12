"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
from typing import List
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        st = ""
        self.board = board
        self.word = word
        self.r = len(board)
        self.c = len(board[0])
        self.solution = [[0] * self.c for _ in range(self.r)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.findsoln(i, j, st):
                        return True
        return False

    def findsoln(self, x, y, st):
        if x < 0 or y < 0 or x >= self.r or y >= self.c or self.solution[x][y] == 1:
            return False
        self.solution[x][y] = 1
        st += self.board[x][y]
        if st == self.word:
            return True
        if st != self.word[:len(st)]:
            self.solution[x][y] = 0
            return False
        if self.findsoln(x + 1, y, st):
            return True
        if self.findsoln(x - 1, y, st):
            return True
        if self.findsoln(x, y + 1, st):
            return True
        if self.findsoln(x, y - 1, st):
            return True
        self.solution[x][y] = 0
        return False
obj=Solution()
res=obj.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")
print(res)
