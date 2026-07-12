"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
from typing import List
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s) - 1
        for i in range(len(s) // 2):
            if i == l:
                break
            temp = s[l]
            s[l] = s[i]
            s[i] = temp
            l -= 1

obj=Solution()
res=obj.reverseString(["h","e","l","l","o"])
print(res)
