class Solution:
    def maxDepth(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        depth = 0    
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                depth = max(depth,len(stack))
            elif s[i] ==')':
                stack.pop()
        return depth            



        