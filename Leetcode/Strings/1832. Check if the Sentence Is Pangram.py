class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l=[0]*26
        for i in sentence:
            l[ord(i)-97]=1
        for i in l:
            if i==0:
                return False
        return True
obj=Solution()
res=obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
print(res)