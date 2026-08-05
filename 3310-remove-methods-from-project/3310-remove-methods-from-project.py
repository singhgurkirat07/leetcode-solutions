from collections import deque
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        grf={}

        for i in range(n):
            grf[i]=[]
        
        for u,v in invocations:
            grf[u].append(v)
        
        q=deque()
        q.append(k)

        v=set()
        sus=set()
        nSus=[]

        while q:
            curr=q.popleft()
            for i in grf[curr]:
                if i not in v:
                    q.append(i)

            v.add(curr)
            sus.add(curr)

        for i in range(n):
            if i not in sus:
                nSus.append(i)
        
        for u,v in invocations:
                if u not in sus and v in sus:
                    return list(range(n))
        return nSus
                