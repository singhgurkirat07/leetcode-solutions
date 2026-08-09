class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        m=1
        suffix=[0]*(len(piles)+1)
        for i in range(len(piles)-1,-1,-1):
            suffix[i]=piles[i]+suffix[i+1]

        memo={}

        def dfs(i,m):
            if i>=len(piles):
                return 0
            collection=0
            taken=0
            if (i,m) in memo:
                return memo[(i,m)]
            
            for x in range(1,2*m+1):
                if i+x>len(piles):
                    break
                taken+=piles[i+x-1]
                opp=dfs(i+x,max(x,m))
                curr=taken+suffix[i+x]-opp
                collection=max(collection,curr)
            memo[(i,m)]=collection
            return collection


        return dfs(0,m)