class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        globalSum = sum(nums)

        for i,num in enumerate(nums):
            if globalSum - 2*left == num:
                return i
            left += num    
        return -1