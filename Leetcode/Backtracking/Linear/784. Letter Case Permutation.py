"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.



Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
"""
class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res=[]
        def backtrack(i,st):
            if i==len(s):
                res.append(st)
                return
            while not s[i].isalpha():
                backtrack(i+1,st+s[i])
                return
            if i>len(s):
                return
            backtrack(i+1,st+s[i].lower())
            backtrack(i+1,st+s[i].upper())
        backtrack(0,"")
        return res
obj=Solution()
res=obj.letterCasePermutation("a1b1c1")
print(res)