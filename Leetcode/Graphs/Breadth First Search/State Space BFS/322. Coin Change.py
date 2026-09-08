"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        steps=0
        queue=deque([])
        visited=set([])
        if not amount:
            return 0
        for num in coins:
            queue.append(num)
            visited.add(num)
        while queue:
            size=len(queue)
            for _ in range(size):
                amt=queue.popleft()
                if amt==amount:
                    return steps+1
                for coin in coins:
                    new_amt=coin+amt
                    if new_amt<=amount and new_amt not in visited:
                        queue.append(new_amt)
                        visited.add(new_amt)
            steps+=1
        return -1
obj=Solution()
res=obj.coinChange([1,2,5],3)
print(res)
