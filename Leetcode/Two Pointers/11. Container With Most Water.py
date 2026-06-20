class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        m = 0
        while left <= right:
            l = right - left
            b = min(height[left], height[right])
            a = l * b
            if a > m:
                m = a
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return m
obj=Solution()
res=obj.maxArea([1,8,6,2,5,4,8,3,7])
print(res)
