"""
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.



Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        i = 0
        ans = 0
        while i < len(s):
            ch = s[i]
            if ch == "(":
                stack.append(ch)
                i += 1
            else:
                if i + 1 < len(s) and s[i] == s[i + 1]:
                    if stack:
                        stack.pop()
                    else:
                        ans += 1
                    i = i + 2
                else:
                    if stack:
                        ans += 1
                        stack.pop()
                    else:
                        ans += 2
                    i += 1
        if stack:
            ans += len(stack) * 2
        return ans
obj=Solution()
res=obj.minInsertions("(())")
print(res)

