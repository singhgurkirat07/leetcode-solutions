from math import gcd
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        def count( leftFreq):
            total = sum(leftFreq.values())

            ans = 1

            for f in leftFreq.values():
                if f == 0:
                    continue

             # Multiply by (total choose f)
                for x in range(1, f + 1):
                    num = total - f + x
                    den = x

                    g = gcd(num, den)
                    num //= g
                    den //= g

                    g = gcd(ans, den)
                    ans //= g
                    den //= g

                    ans = ans * num // den

                total -= f
            return ans


        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        
        leftFreq={}
        for ch in sorted(freq):
            leftFreq[ch]=freq[ch]//2
        

        left=""

        currentCount = count(leftFreq)
        if currentCount < k:
            return ""
        remainingLetters = sum(leftFreq.values())
        while remainingLetters>0:
            for ch in sorted(leftFreq):
                if leftFreq[ch]>0:
                    newCount = currentCount * leftFreq[ch] // remainingLetters
                    if newCount>=k:
                        left+=ch
                        leftFreq[ch]-=1
                        currentCount=newCount
                        remainingLetters-=1
                        break
                    else:
                        k -= newCount

        middle=""

        for ch in sorted(freq):
            if freq[ch]%2==1:
                middle=ch
                break

        return left+middle+left[::-1]

        