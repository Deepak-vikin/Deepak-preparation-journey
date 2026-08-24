"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.



Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
"""
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue=deque([startGene])
        target=endGene
        mut=0
        visited=set()
        a=["A","C","G","T"]
        while queue:
            for _ in range(len(queue)):
                curr=queue.popleft()
                if curr==target:
                    return mut
                for i in range(len(curr)):
                    c=curr[i]
                    for j in a:
                        if c==j:
                            continue
                        next_state=curr[:i]+j+curr[i+1:]
                        if next_state not in visited and next_state in bank:
                            visited.add(next_state)
                            queue.append(next_state)
            mut+=1
        return -1
obj=Solution()
print(obj.minMutation("AACCGGTA","AACCGGTA"),["AACCGGTA"])

