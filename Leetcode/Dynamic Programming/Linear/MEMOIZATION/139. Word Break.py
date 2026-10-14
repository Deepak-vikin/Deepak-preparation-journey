"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
"""
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n=len(s)
        dp=[-1]*n
        def solve(num):
            if num==n:
                return True
            if dp[num]!=-1:
                return dp[num]
            for j in range(num,n):
                if s[num:j+1] in wordDict and solve(j+1):
                    dp[num]=True
                    return True
            dp[num]=False
            return False
        return solve(0)
obj=Solution()
res=obj.wordBreak("leetcode",["leet","code"])
print(res)