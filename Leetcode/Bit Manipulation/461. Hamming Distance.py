"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.



Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        st=x^y
        count=0
        while st!=0:
            st=st&(st-1)
            count+=1
        return count

obj=Solution()
print(obj.hammingDistance(1,2))
