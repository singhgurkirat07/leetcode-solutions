class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        ans = 0
        open = 0
        close = 0

        for right in range(len(s)):
            if s[right] == "(":
                open += 1
            else:
                close += 1

            if close == open:
                ans = max(ans, right - left + 1)

            if close > open:
                left = right + 1
                open = 0
                close = 0

        left = len(s) - 1
        open = 0
        close = 0

        for right in range(len(s) - 1, -1, -1):
            if s[right] == "(":
                open += 1
            else:
                close += 1

            if close == open:
                ans = max(ans, left - right + 1)

            if open > close:
                left = right - 1
                open = 0
                close = 0

        return ans