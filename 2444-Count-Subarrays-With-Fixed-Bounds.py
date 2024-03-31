class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        maxi,mini,badi,n = -1,-1,-1,len(nums)
        ans = 0
        for i in range(n):
                if nums[i] < minK or nums[i] > maxK:
                        badi = i
                if nums[i] == minK:
                        mini = i
                if nums[i] == maxK:
                        maxi = i
                ans += max(0,min(mini,maxi)-badi)
        return ans    