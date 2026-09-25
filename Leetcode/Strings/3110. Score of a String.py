"""
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.



Example 1:

Input: s = "hello"

Output: 13

Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
"""
class Solution:
    def scoreOfString(self, s: str) -> int:
        scores=[]
        for i in s:
            scores.append(ord(i))
        ans=0
        for i in range(1,len(scores)):
            ans+=abs(scores[i]-scores[i-1])
        return ans
obj=Solution()
res=obj.scoreOfString("hello")
print(res)