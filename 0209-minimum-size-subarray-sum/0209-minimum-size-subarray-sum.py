class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        high=0
        minlenwindow=float('inf')
        curr_sum=0

        while(high<len(nums)):

            curr_sum+=nums[high]
            high+=1

            while(curr_sum>=target):
                minlenwindow=min(minlenwindow,high-low)
                curr_sum-=nums[low]
                low+=1
        return minlenwindow if minlenwindow!=float('inf') else 0