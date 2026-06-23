"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        r = ""
        f = 0
        for i in s:
            if i.isalnum():
                r += i
        i = 0
        j = len(r) - 1
        r = r.lower()
        while i <= j:
            if r[i] == r[j]:
                f = 1
                i += 1
                j -= 1
            else:
                return False
        return True

obj=Solution()
res=obj.isPalindrome("abcd")
print(res)
