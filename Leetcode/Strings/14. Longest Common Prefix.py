"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
from typing import List
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res=""
        for i in range(len(strs[0])):
            if strs[0][i]==strs[len(strs)-1][i]:
                res+=strs[0][i]
            else:
                return res
        return res
obj=Solution()
res=obj.longestCommonPrefix(["flower","flow","flight"])
print(res)
