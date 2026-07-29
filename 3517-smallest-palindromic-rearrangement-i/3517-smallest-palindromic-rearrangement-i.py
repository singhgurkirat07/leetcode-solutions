class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        
        left=""
        for ch in sorted(freq):
            left+= ch * (freq[ch]//2)
        
        right=left[::-1]

        middle=""
        for ch in sorted(freq):
            if freq[ch]%2==1:
                middle=ch
        
        return left+middle+right