"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.



Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(x.isupper() for x in word) or (word[0].isupper() and all(x.islower() for x in word[1:])) or all(x.islower() for x in word):
            return True
        return False
obj=Solution()
res=obj.detectCapitalUse("USA")
print(res)