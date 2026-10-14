"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
"""
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        n=len(s)
        res=[]
        def solve(num,st):
            if num==n:
                res.append(" ".join(st))
                return False
            for j in range(num,n):
                if s[num:j+1] in wordDict and solve(j+1,st+[s[num:j+1]]):
                    return False
            return False
        solve(0,[])
        return res
obj=Solution()
res=obj.wordBreak("catsanddog",["cat","sand","dog"])
print(res)