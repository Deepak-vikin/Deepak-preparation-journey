"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l=[0]*26
        for i in sentence:
            l[ord(i)-97]=1
        for i in l:
            if i==0:
                return False
        return True
obj=Solution()
res=obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
print(res)