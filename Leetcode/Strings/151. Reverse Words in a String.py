"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        i=0
        j=len(s)-1
        while i<=j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return " ".join(s)
obj=Solution()
res=obj.reverseWords("the sky is blue")
print(res)