"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([beginWord])
        visited = set([beginWord])
        steps = 0
        chars = "abcdefghijklmnopqrstuvwxyz"
        words = set(wordList)
        if endWord not in wordList:
            return 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return steps + 1
                for i in range(len(curr)):
                    char = curr[i]
                    for j in chars[:ord(char) - 97] + chars[ord(char) - 96:]:
                        new_state = curr[:i] + j + curr[i + 1:]
                        if new_state in words and new_state not in visited:
                            visited.add(new_state)
                            queue.append(new_state)
            steps += 1
        return 0
obj=Solution()
res=obj.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])
print(res)