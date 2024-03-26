class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        for i in range(len(nums)):
            if nums[i] >= 1 and nums[i] == ans:
                ans += 1
            elif nums[i] > ans: return ans        
        n = nums[len(nums)-1]+1
        return 1 if n < 1 else n         
        