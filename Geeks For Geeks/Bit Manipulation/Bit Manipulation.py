"""
Given a 32 bit unsigned integer num and an integer i. Perform following operations on the number -

1. Get ith bit

2. Set ith bit

3. Clear ith bit

Note : For better understanding, we are starting bits from 1 instead 0. (1-based). You have to print space three space separated values ( as shown in output without a line break) and do not have to return anything.

Examples :

Input: 70 3
Output: 1 70 66
Explanation: Bit at the 3rd position from LSB is 1. (1 0 0 0 1 1 0) .The value of the given number after setting the 3rd bit is 70. The value of the given number after clearing 3rd bit is 66. (1 0 0 0 0 1 0)
"""
class Solution:
    def bitManipulation(self, num, i):
        # Code here
        i-=1
        a=0
        if num&(1<<i)==0:
            a=0
        else:
            a=1
        print(a,num|(1<<i),num & (~(1<<i)))
obj=Solution()
obj.bitManipulation(70,3)