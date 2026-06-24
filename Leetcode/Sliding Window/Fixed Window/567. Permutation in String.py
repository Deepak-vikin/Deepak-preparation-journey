"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1=[0]*26
        for i in s1:
            arr1[ord(i)-97]+=1
        k=len(s1)
        arr2=[0]*26
        if len(s1)>len(s2):
            return False
        for i in range(k):
            arr2[ord(s2[i])-97]+=1
        for i in range(k,len(s2)):
            if arr1==arr2:
                return True
            arr2[ord(s2[i])-97]+=1
            arr2[ord(s2[i-k])-97]-=1
        if arr1==arr2:
            return True
        return False
obj=Solution()
res=obj.checkInclusion("ab","eidbaooo")
print(res)