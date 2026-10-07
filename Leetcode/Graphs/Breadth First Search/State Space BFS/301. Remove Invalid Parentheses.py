"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.



Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res=[]
        def isvalid(s):
            balance=0
            for ch in s:
                if ch=="(":
                    balance+=1
                if ch==")":
                    balance-=1
                if balance<0:
                    return False
            return balance==0
        queue=deque([s])
        visited = set([s])
        while queue:
            next_set=[]
            for curr in queue:
                if isvalid(curr):
                    res.append(curr)
            if res:
                return res
            for curr in queue:
                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue
                    next=curr[:i]+curr[i+1:]
                    if next not in visited:
                        visited.add(next)
                        next_set.append(next)
            queue=next_set
obj=Solution()
res=obj.removeInvalidParentheses("()())()")
print(res)
