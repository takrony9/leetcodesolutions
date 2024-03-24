class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        res = zeros = 0

        for num in nums:
            if num == 0: 
                zeros += 1
            else:
                zeros = 0
            res += zeros
                
        return res