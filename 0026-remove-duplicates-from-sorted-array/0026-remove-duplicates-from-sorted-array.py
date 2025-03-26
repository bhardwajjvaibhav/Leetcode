class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0

        if n==0:
            print("The Arrauy is Empty")
        else:
            for j in range(1,n):
                if nums[i]!=nums[j]:
                    nums[i+1]=nums[j]
                    i+=1
            
        return i+1
    