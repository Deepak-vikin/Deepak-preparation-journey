"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.m = len(image)
        self.n = len(image[0])
        self.solution = [[0] * self.n for _ in range(self.m)]
        self.image = image
        self.color = color
        for i in range(self.m):
            for j in range(self.n):
                if i == sr and j == sc:
                    self.nx = self.image[sr][sc]
                    self.findsoln(i, j, self.solution)
                    return image

    def findsoln(self, x, y, solution):
        if x < 0 or y < 0 or x >= self.m or y >= self.n or solution[x][y] == 1 or self.image[x][y] != self.nx:
            return
        solution[x][y] = 1
        self.image[x][y] = self.color
        self.findsoln(x + 1, y, solution)
        self.findsoln(x - 1, y, solution)
        self.findsoln(x, y + 1, solution)
        self.findsoln(x, y - 1, solution)
        return
obj=Solution()
res=obj.floodFill([[1,1,1],[1,1,0],[1,0,1]],2,2)
print(res)
