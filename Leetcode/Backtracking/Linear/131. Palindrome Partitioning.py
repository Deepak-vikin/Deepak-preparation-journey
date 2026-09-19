"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res=[]
        def dfs(i,path):
            if i==len(s):
                res.append(path.copy())
                return
            for j in range(i,len(s)):
                sub=s[i:j+1]
                if sub==sub[::-1]:
                    path.append(sub)
                    dfs(j+1,path)
                    path.pop()
        dfs(0,[])
        return res
obj=Solution()
res=obj.partition("aab")
print(res)