class Solution:
    def minimumPushes(self, word: str) -> int:
        freq={}
        for i in word:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        freq=sorted(freq.values(),reverse=True)

        ans = 0

        for i in range(len(freq)):
            ans += freq[i] * (i // 8 + 1)

        return ans