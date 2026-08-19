class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved={}
        total=0

        for x in reservedSeats:
            if x[0] in reserved:
                reserved[x[0]].append(x[1])
            else:
                reserved[x[0]]=[]
                reserved[x[0]].append(x[1])

        
        for row in reserved:
            left=True
            middle=True
            right=True
            curr=0
            for seat in reserved[row]:
                if seat in [2,3,4,5]:
                    left=False
                if seat in [4,5,6,7]:
                    middle=False
                if seat in [6,7,8,9]:
                    right=False
            
            if left and right:
                curr=2
            elif middle or left or right:
                curr=1
            else:
                curr=0
            total+=curr
        total+=(n-len(reserved))*2
        return total