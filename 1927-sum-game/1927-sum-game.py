class Solution:
    def sumGame(self, num: str) -> bool:
        left_sum=0
        right_sum=0
        leftq=0
        rightq=0

        for x in num[:len(num)//2]:
            if x=="?":
                leftq+=1
            else:
                left_sum+=int(x)
        for x in num[len(num)//2:]:
            if x=="?":
                rightq+=1
            else:
                right_sum+=int(x)
            
        if left_sum==right_sum:
            return leftq!=rightq
        

        return 2 * (left_sum - right_sum) != 9 * (rightq - leftq)