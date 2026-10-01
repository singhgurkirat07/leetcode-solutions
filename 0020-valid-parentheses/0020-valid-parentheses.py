class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opening=['(','{','[']
        closing=[')','}',']']
        if len(s)==0:
            return False

        for st in s:
            if st in opening:
                stack.append(st)
            elif st in closing:
                if not stack:
                    return False
                if st == ')' and stack[-1] == '(':
                    stack.pop()
                elif st == ']' and stack[-1] == '[':
                    stack.pop()
                elif st == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        return not stack