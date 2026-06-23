"""
Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        i=0
        j=len(x)-1
        while(i<=j):
            if x[i]==x[j]:
                f=1
                i+=1
                j-=1
            else:
                f=0
                break
        if f==1:
            return True
        else:
            return False
obj = Solution()
print(obj.isPalindrome(121))