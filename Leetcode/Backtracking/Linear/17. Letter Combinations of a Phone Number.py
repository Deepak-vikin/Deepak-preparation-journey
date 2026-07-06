"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        f={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        arr=[]
        for i in digits:
            arr.append(f[int(i)])
        res=[]
        def solve(i,path):
            if len(path)==len(arr):
                res.append(path)
                return
            for ch in arr[i]:
                solve(i+1,path+ch)
        solve(0,"")
        return res
obj=Solution()
res=obj.letterCombinations("23")
print(res)
