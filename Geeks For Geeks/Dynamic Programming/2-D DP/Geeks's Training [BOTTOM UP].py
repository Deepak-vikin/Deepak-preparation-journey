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
        dp=[[-1]*4 for _ in range(n)]
        dp[0][0]=max(mat[0][1],mat[0][2])
        dp[0][1]=max(mat[0][0],mat[0][2])
        dp[0][2]=max(mat[0][1],mat[0][0])
        dp[0][3]=max(mat[0][0],mat[0][1],mat[0][2])
        for day in range(1,n):
            for last in range(4):
                dp[day][last]=0
                for task in range(3):
                    if task!=last:
                        point=mat[day][task]+dp[day-1][task]
                        dp[day][last]=max(dp[day][last],point)
        return dp[n-1][3]
obj=Solution()
res=obj.maximumPoints([[8,7,1],[9,2,1]])
print(res)