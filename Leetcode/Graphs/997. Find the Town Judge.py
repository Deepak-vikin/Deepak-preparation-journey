"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
"""
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        graph={}
        indegree={i:0 for i in range(1,n+1)}
        outdegree={i:0 for i in range(1,n+1)}
        for u,v in trust:
            indegree[v]+=1
            outdegree[u]+=1
        for i in range(1,n+1):
            if indegree[i]==(n-1) and outdegree[i]==0:
                return i
        return -1
obj=Solution()
res=obj.findJudge(2,[[1,0],[0,1]])
print(res)


