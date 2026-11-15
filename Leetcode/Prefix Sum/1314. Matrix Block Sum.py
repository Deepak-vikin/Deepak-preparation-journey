"""
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.


Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
"""
class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        n=len(mat)
        m=len(mat[0])
        pref_mat=[[0]*m for _ in range(n)]
        pref_mat[0][0]=mat[0][0]
        for i in range(1,m):
            pref_mat[0][i]=mat[0][i]+pref_mat[0][i-1]
        for i in range(1,n):
            pref_mat[i][0]=mat[i][0]+pref_mat[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                pref_mat[i][j]=mat[i][j]+pref_mat[i-1][j]+pref_mat[i][j-1]-pref_mat[i-1][j-1]
        res=[]
        for i in range(n):
            ans=[]
            for j in range(m):
                r1=max(0,i-k)
                c1=max(0,j-k)
                r2=min(n-1,i+k)
                c2=min(m-1,j+k)
                total=pref_mat[r2][c2]
                if r1>0:
                    total-=pref_mat[r1-1][c2]
                if c1>0:
                    total-=pref_mat[r2][c1-1]
                if r1>0 and c1>0:
                    total+=pref_mat[r1-1][c1-1]
                ans.append(total)
            res.append(ans)
        return res
obj=Solution()
res=obj.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 3)
print(res)