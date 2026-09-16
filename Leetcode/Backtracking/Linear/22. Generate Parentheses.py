"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def backtrack(path,open,close):
            if len(path)==2*n:
                ans.append(path)
                return
            if open<n:
                backtrack(path+"(",open+1,close)
            if close<open:
                backtrack(path+")",open,close+1)
        backtrack("",0,0)
        return ans
obj=Solution()
print(obj.generateParenthesis(3))
print(obj.generateParenthesis(2))
print(obj.generateParenthesis(1))