class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        f1={}
        f2={}
        for i in s:
            if i in f1:
                f1[i]+=1
            else:
                f1[i]=1
        for i in t:
            if i in f2:
                f2[i]+=1
            else:
                f2[i]=1
        for i in f1:
            if i not in f2:
                return False
            else:
                if f1[i]!=f2[i]:
                    return False
        return True
obj=Solution()
res=obj.isAnagram("cbaebabacd","abc")
print(res)