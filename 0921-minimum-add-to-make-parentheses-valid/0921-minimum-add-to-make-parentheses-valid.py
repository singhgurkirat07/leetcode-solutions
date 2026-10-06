class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        ans=0
        open=0

        for p in s:
            if p=='(':
                open+=1
            else:
                if open>0:
                    open-=1
                else:
                    ans+=1
        return ans+open