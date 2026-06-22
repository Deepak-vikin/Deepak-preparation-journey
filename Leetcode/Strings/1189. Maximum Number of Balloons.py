"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        l = [0] * 26
        res = "ballloon"
        for i in text:
            if i in res:
                l[ord(i) - ord('a')] += 1
        return min(l[0], l[1], l[11] // 2, l[13], l[14] // 2)

obj=Solution()
res =obj.maxNumberOfBalloons("nlaebolko")
print(res)