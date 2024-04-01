class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        ans = 0
        for i in range(len(s)):
            if s[i]!= ' ':
                count +=1
                ans = count
            else: 
                count =0
        return ans    

        