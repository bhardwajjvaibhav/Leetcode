class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        count=[]
        l,r=0,len(nums)-1
        if target not in nums:
            return [-1,-1]
        elif len(nums)==1:
            return [0,0]
        
            
        else:
            while(l<=r):
                mid=(l+r)//2

            

                if nums[mid]==target:
                    if mid not in count:
                        count.append(mid)
                    l=l+1
                
            
                elif nums[mid]<target:
                    l=l+1

                else:
                    r=r-1
            return count
        