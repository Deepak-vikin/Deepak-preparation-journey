"""
Geek is attending a training program for n days. Each day he must perform exactly one of three activities: Running, Fighting, or Learning. Each activity earns a certain number of merit points, which can differ from day to day.
To improve all his skills, Geek cannot perform the same activity on two consecutive days.
Given a 2D matrix mat[][] of size n × 3, where for the i-th day:

mat[i][0] is the merit points for Running
mat[i][1] is the merit points for Fighting
mat[i][2] is the merit points for Learning
Return the maximum total merit points Geek can earn over the n days.

Example:

Input: mat[][] = [[8, 7, 1],[9, 2, 1]]
Output: 16
Explanation: Picking the best activity on day 1 (Running, 8) blocks Running on day 2,
so the best he could then get is Fighting (2), giving 10.
Instead, Geek does Fighting on day 1 (7) and Running on day 2 (9), giving 7 + 9 = 16.
"""
class Solution:
    def maximumPoints(self, mat):
        n=len(mat)
        dp=[[-1]*3 for _ in range(n)]
        def func(curr,last):
            if curr==0:
                maxi=0
                for i in range(3):
                    if i!=last:
                        maxi=max(maxi,mat[0][i])
                return maxi
            if dp[curr][last]!=-1:
                return dp[curr][last]
            max_sum=0
            for i in range(3):
                if i!=last:
                    curr_sum=mat[curr][i]+func(curr-1,i)
                    max_sum=max(max_sum,curr_sum)
            dp[curr][last]=max_sum
            return dp[curr][last]
        return func(n-1,-1)
obj=Solution()
res=obj.maximumPoints([[8, 7, 1],[9, 2, 1]])
print(res)