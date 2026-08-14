class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        s=list(s)
        leng=0
        freq={}
        left=0

        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]]=1
            else:
                freq[s[right]]+=1
                if freq[s[right]]>2:
                    while freq[s[right]]>2:
                        freq[s[left]]-=1
                        left+=1
            leng=max(leng,right-left+1)

        return leng