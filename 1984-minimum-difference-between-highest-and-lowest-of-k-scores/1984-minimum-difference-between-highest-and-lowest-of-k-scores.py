class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        min_diff=float('inf')
        nums.sort()
        

        if k==1:
            return 0
        
        else:

            for i in range(len(nums)-k+1):
                min_diff=min(min_diff,nums[i+k-1]-nums[i])
        return min_diff
