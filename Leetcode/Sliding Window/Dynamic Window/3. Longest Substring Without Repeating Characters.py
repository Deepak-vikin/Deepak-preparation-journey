"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        se = set()
        m = 0
        for right in range(len(s)):
            while s[right] in se:
                se.remove(s[left])
                left += 1
            se.add(s[right])
            m = max(m, right - left + 1)
        return m
obj=Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))
