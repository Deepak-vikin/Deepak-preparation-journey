"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        min_len=min(len(word1),len(word2))
        for i in range(min_len):
            s+=word1[i]
            s+=word2[i]
        if len(word1)>len(word2):
            for i in range(min_len,len(word1)):
                s+=word1[i]
        else:
            for i in range(min_len,len(word2)):
                s+=word2[i]
        return s
obj=Solution()
res=obj.mergeAlternately("abcd","pqr")
print(res)
