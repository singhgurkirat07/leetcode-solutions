class Solution:
    def countCommas(self, n: int) -> int:
        if n<=999:
            return 0
        cnt=0

        for num in range(1000,n+1):
            while len(str(num))>3:
                num//=1000
                cnt+=1

        return cnt