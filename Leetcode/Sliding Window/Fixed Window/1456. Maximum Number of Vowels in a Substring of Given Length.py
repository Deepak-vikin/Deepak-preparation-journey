"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        m=0
        c=0
        for i in range(k):
            if s[i] in "aeiou":
                c+=1
        m=c
        for i in range(k,len(s)):
            if s[i] in "aeiou":
                c+=1
            if s[i-k] in "aeiou":
                c-=1
            m=max(c,m)
        return m

obj=Solution()
res=obj.maxVowels("abciiidef", 3)
print(res)