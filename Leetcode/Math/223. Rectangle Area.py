"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:
Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def area(ax1, ax2, ay1, ay2):
            length1 = ax2 - ax1
            breadth1 = ay2 - ay1
            area = length1 * breadth1
            return area

        area1 = area(ax1, ax2, ay1, ay2)
        area2 = area(bx1, bx2, by1, by2)
        total_area = area1 + area2
        cx1, cy1 = (max(ax1, bx1), max(ay1, by1))
        cx2, cy2 = (min(ax2, bx2), min(ay2, by2))
        common_area = max(0, cx2 - cx1) * max(0, cy2 - cy1)
        return total_area - common_area
obj=Solution()
res = obj.computeArea(-3,0,3,4,0,-1,9,2)
print(res)