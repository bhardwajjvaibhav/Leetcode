class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res=[]
        i=0
        j=i+1
        arr.sort()
        n=len(arr)
        mindiff=float('inf')

        for i in range(n-1):
            diff = abs (arr[i]-arr[i+1])
           

            if diff <mindiff:
                mindiff=diff
                res = [[arr[i], arr[i + 1]]]
            
            elif diff==mindiff:

                res.append([arr[i],arr[i+1]])

        return res

                      
