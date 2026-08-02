class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo={}
        def advantage(left,right):
            if left==right:
                return piles[left]
            
            if (left,right) in memo:
                return memo[(left,right)]
            
            take_left=piles[left]-advantage(left+1,right)
            take_right=piles[right]-advantage(left,right-1)
            
            memo[(left,right)]=max(take_left,take_right)
            
            return max(take_left,take_right)
        
        return advantage(0,len(piles)-1)>0