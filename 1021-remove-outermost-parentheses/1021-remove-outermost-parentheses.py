class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        depth=0

        for b in s:
            if b=="(":
                if depth==0:
                    depth+=1
                    continue
                    
                depth+=1
                ans+=b
            
            if b==")":
                depth-=1

                if depth==0:
                    continue

                ans+=b
                    
        return ans