class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def solve(open,close,n,curr):

            if open==n and close==n:
                ans.append(curr)
                return
            
            if open < n:
                solve(open + 1, close, n, curr + "(")
            if close < open:
                solve(open, close + 1, n, curr + ")")
            
        solve(0,0,n,"")
        return ans
