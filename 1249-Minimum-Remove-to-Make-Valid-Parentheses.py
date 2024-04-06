

import collections
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        stack = []
        n=len(s)
        i=0
        while i <n:
            if s[i] == '(':
                ans.append(i)
                stack.append(s[i])
            elif s[i] == ')':
                if stack:
                    stack.pop()
                    ans.pop()
                else:
                    s = s[:i] + s[i+1:]
                    n -=1
                    i-=1
            i +=1        
        while stack:
            stack.pop()
            index = ans.pop()
            s = s[:index] + s[index+1:]
        return s                        
                
        