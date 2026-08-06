class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+10):
            if (math.prod(map(int, str(i))))%t==0:
                return i