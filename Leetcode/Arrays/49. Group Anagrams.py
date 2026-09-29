"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        freq = {}
        for word in strs:
            chars = [0] * 26
            for i in word:
                chars[ord(i) - ord('a')] += 1
            freq.setdefault(tuple(chars), []).append(word)
        for lst in freq.values():
            res.append(lst)
        return res
obj=Solution()
res=obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(res)






