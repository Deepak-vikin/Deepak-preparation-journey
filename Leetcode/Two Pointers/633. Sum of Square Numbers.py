"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.



Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
"""
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=math.ceil(math.sqrt(c))
        while left<=right:
            s=left*left+right*right
            if s==c:
                return True
            if s<c:
                left+=1
            else:
                right-=1
        return False
obj=Solution()
print(obj.judgeSquareSum(5))
