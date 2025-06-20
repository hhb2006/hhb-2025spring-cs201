class Solution:
    def resultingString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if stack and abs(ord(stack[-1]) - ord(s[i])) in {1, 25}:
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)