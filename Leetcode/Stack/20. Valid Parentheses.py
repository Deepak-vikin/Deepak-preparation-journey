"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.
3.Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in range(len(s)):
            if s[i] in "[{(":
                lst.append(s[i])
            else:
                if not lst:
                    return False
                if s[i] is ']':
                    if lst[-1] is '[':
                        lst.pop()
                    else:
                        return False
                if s[i] is ')':
                    if lst[-1] is '(':
                        lst.pop()
                    else:
                        return False
                if s[i] is '}':
                    if lst[-1] is '{':
                        lst.pop()
                    else:
                        return False
        return not lst


obj=Solution()
print(obj.isValid("()"))