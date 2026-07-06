"""
Given a string s, which may contain duplicate characters, your task is to generate and return an array of all unique permutations of the string. You can return your answer in any order.

Examples:

Input: s = "ABC"
Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
Explanation: Given string ABC has 6 unique permutations.
"""

class Solution:
    def findPermutation(self, s):
        s=sorted(s)
        s="".join(s)
        res=[]
        used=[0]*len(s)
        def perm(path):
            if len(path)==len(s):
                res.append(path)
                return
            for i in range(len(s)):
                if used[i]:
                    continue
                if i>0 and s[i]==s[i-1] and not used[i-1]:
                    continue
                used[i]=1
                perm(path+s[i])
                used[i]=0
        perm("")
        return res
obj=Solution()
res=obj.findPermutation("ABC")
print(res)