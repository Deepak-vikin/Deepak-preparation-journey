"""
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.



Example 1:


Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
Example 2:

Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4
"""
class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        dp={}
        n=len(books)
        def func(i):
            if i==n:
                return 0
            if i in dp:
                return dp[i]
            thick=0
            height=0
            ans=float("inf")
            for j in range(i,n):
                thick+=books[j][0]
                if thick>shelfWidth:
                    break
                height=max(height,books[j][1])
                ans=min(ans,height+func(j+1))
            dp[i]=ans
            return ans
        return func(0)
obj=Solution()
res=obj.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]],shelfWidth=4)
print(res)

