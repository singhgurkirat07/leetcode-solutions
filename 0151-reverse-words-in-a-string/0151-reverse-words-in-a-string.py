class Solution:
    def reverseWords(self, s: str) -> str:
        ans=''
        word=''
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ' :
                if word:
                    word=word[::-1]
                    ans+=word
                    ans+=" "
                    word=""
            else:
                word+=s[i]
        ans+=word[::-1]
        
        return ans.strip()
