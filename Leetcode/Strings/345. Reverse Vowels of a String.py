"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        v="aeiouAEIOU"
        s=list(s)
        while i<=j:
            while s[i] not in v and i<j:
                i+=1
            while s[j] not in v and i<j:
                j-=1
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        res=""
        for i in s:
            res+=i
        return res
obj=Solution()
res=obj.reverseVowels("IceCreAm")
print(res)