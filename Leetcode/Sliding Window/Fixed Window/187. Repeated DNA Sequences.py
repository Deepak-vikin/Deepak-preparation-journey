"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.



Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res=[]
        f={}
        for i in range(len(s)-9):
            st=s[i:i+10]
            if st in f:
                if st not in res:
                    res.append(st)
                f[st]+=1
            else:
                f[st]=1
        return res
obj=Solution()
res=obj.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTT")
print(res)
