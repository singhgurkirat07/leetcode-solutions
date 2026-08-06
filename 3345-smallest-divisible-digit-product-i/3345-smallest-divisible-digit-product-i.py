class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,100):
            if (math.prod(map(int, str(i))))%t==0:
                return i
        return 100