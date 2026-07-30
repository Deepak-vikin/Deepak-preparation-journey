"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = []
        for i in range(1, 10):
            arr.append(i)
        res = []

        def solve(i, s, path):
            if s > n:
                return
            if s == n:
                if len(path) == k:
                    res.append(path)
                return
            if i == 9:
                return
            solve(i + 1, s + arr[i], path + [arr[i]])
            solve(i + 1, s, path)

        solve(0, 0, [])
        return res
obj = Solution()
res = obj.combinationSum3(3, 4)
print(res)