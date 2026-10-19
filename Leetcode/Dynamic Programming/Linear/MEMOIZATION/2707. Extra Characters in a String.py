"""
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.



Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.
"""
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp=[-1]*len(s)
        n=len(s)
        def solve(num):
            if num==n:
                return 0
            if dp[num]!=-1:
                return dp[num]
            ans=1+solve(num+1)
            for i in range(num,n):
                if s[num:i+1] in dictionary:
                    ans=min(ans,solve(i+1))
            dp[num]=ans
            return ans
        return solve(0)
obj=Solution()
res=obj.minExtraChar("leetcode",["leet","code","leetcode"])
print(res)
