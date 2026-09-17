"""
You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.



Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
"""


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        pref = [0] * n
        suff = [0] * n
        left = 0
        s = 0
        for right in range(n):
            s += arr[right]
            while s > target:
                s -= arr[left]
                left += 1
            if s == target:
                l = right - left + 1
                if right == 0 or pref[right - 1] == 0:
                    pref[right] = l
                else:
                    pref[right] = l if right == 0 else min(pref[right - 1], l)
            elif right == 0:
                pref[right] = 0
            else:
                pref[right] = pref[right - 1]
        right = n - 1
        s = 0
        for left in range(n - 1, -1, -1):
            s += arr[left]
            while s > target:
                s -= arr[right]
                right -= 1
            if s == target:
                l = right - left + 1
                if left == n - 1 or suff[left + 1] == 0:
                    suff[left] = l
                else:
                    suff[left] = l if left == n - 1 else min(suff[left + 1], l)
            elif left == n - 1:
                suff[left] = 0
            else:
                suff[left] = suff[left + 1]
        ans = float("inf")
        for i in range(n - 1):
            if pref[i] and suff[i + 1]:
                ans = min(ans, pref[i] + suff[i + 1])
        if ans != float("inf"):
            return ans
        else:
            return -1
obj=Solution()
res=obj.minSumOfLengths([3,2,2,4,3],3)
print(res)