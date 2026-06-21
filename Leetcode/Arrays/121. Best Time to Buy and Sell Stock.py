class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        i=0
        j=1
        while i<len(prices) and j<len(prices):
            if prices[i]>prices[j]:
                i=j
            else:
                f=prices[j]-prices[i]
                if f>p:
                    p=f
            j+=1
        return p
obj=Solution()
print(obj.maxProfit([1,2,3,4,5]))