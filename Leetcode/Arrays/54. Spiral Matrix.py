"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

from typing import List
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row=len(matrix)
        col=len(matrix[0])
        top=0
        right=col-1
        left=0
        bottom=row-1
        l=[]
        while(top<=bottom and left<=right):
            for i in range(left,right+1):
                l.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                l.append(matrix[i][right])
            right-=1
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    l.append(matrix[bottom][i])
                bottom-=1
            if (left<=right):
                for i in range(bottom,top-1,-1):
                    l.append(matrix[i][left])
                left+=1
        return l
obj=Solution()
res=obj.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)
