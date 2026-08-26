"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.


Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
"""
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=""
        num=str(num)
        for i in range(len(num)-2):
            if num[i:i+3] in ["000","111","222","333","444","555","666","777","888","999"]:
                if res!="":
                    res=str(max(int(res),int(num[i:i+3])))
                    if res=="0":
                        res="000"
                else:
                    res=num[i:i+3]
        return res
obj=Solution()
res = obj.largestGoodInteger("67771333")
print(res)
