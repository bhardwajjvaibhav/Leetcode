class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0

        for i in range(n):
            if count==0:
                count+=1
                el=nums[i]
            
            elif nums[i]==el:
                count+=1

            else:
                count-=1
        count+=1
        for i in range(n):
            if nums[i]==el:
                count+=1
        
        if count>n/2:
            return el
        else:
             return 0
