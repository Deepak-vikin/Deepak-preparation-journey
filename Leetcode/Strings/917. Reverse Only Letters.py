"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.



Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if s[i].isalpha():
                if s[j].isalpha():
                    s[i],s[j]=s[j],s[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        return "".join(s)

obj=Solution()
res=obj.reverseOnlyLetters("ab-cd")
print(res)
