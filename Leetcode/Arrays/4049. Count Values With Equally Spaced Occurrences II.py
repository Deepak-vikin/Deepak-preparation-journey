"""
You are given an integer array nums.

An integer x is called special if:

x appears at least three times in nums.
All occurrences of x are equally spaced in nums. In other words, if all occurrences of x are at indices i1 < i2 < ... < im, then i2 - i1 = i3 - i2 = ... = im - im-1.
Return the number of distinct special integers in nums.



Example 1:

Input: nums = [1,8,1,5,1,5,8,5]

Output: 2

Explanation:

1 is special because it occurs at equally spaced indices 0, 2, and 4.
5 is special because it occurs at equally spaced indices 3, 5, and 7.
8 is not special because it occurs only twice.
Therefore, the answer is 2.
"""
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq={}
        count_freq={}
        for index,num in enumerate(nums):
            freq.setdefault(num,[]).append(index)
            count_freq[num]=count_freq.get(num,0)+1
        count=0
        for curr in freq:
            num=freq.get(curr)
            if count_freq[curr]>=3:
                diff=num[1]-num[0]
                is_common=all(num[i]-num[i-1]==diff for i in range(2,len(num)))
                if is_common:
                    count+=1
        return count
obj=Solution()
res=obj.countSpecialIntegers([1,8,1,5,1,5,8,5])
print(res)