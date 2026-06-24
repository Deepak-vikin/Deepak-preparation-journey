"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        arr1=[0]*26
        res=[]
        for i in range(len(p)):
            arr1[ord(p[i])-97]+=1
        arr2=[0]*26
        if len(p)>len(s):
            return []
        for i in range(k):
            arr2[ord(s[i])-97]+=1
        for i in range(k,len(s)):
            if arr1==arr2:
                res.append(i-k)
            arr2[ord(s[i-k])-97]-=1
            arr2[ord(s[i])-97]+=1
        if arr1==arr2:
            res.append(len(s)-k)
        return res
obj=Solution()
res=obj.findAnagrams("cbaebabacd","abc")
print(res)
