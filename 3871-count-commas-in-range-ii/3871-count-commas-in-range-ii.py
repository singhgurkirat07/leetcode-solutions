class Solution:
    def countCommas(self, n: int) -> int:
        total=0
        leng=len(str(n))

        for num in range(4,leng+1):
            commas=(num-1)//3

            start = 10**(num-1)
            end = min(n,10**num-1)

            if start<=end:
                count=end-start+1
                total+=count*commas
        
        return total