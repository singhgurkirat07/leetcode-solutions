class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0#min possible num of unmatched open
        high = 0#max possible num of unmatched open

        for c in s:

            if c == '(':
                low += 1
                high += 1

            elif c == ')':
                low -= 1
                high -= 1

            else:  
                low -= 1      
                high += 1     

            low = max(0, low)

            if high < 0:
                return False

        return low == 0