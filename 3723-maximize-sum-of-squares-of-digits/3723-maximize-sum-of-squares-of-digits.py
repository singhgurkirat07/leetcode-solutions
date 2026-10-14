class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9*num:
            return ""
        ans=""

        while sum>0:
            if sum >=9:
                ans+="9"
                sum-=9
            else:
                ans+=str(sum)
                sum=0
        
        ans+="0"*(num-len(ans))

        return ans