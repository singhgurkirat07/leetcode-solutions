class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo={}
        def solve(n):
            if n==0:
                return False

            if n in memo:
                return memo[n]
            root=int(sqrt(n))
            while root>0:
                curr_n=n-(root*root)
                if not solve(curr_n):
                    memo[n]=True
                    return True
                root-=1
            memo[n]=False
            return False
        return solve(n)
            