class Solution:
    def maxDifference(self, s: str) -> int:
        count={}
        odd=0
        even=0

        for i in range(len(s)):
            if s[i] in count:
                count[s[i]]+=1
            else:
                count[s[i]]=1
                
        sorted_dict=dict(sorted(count.items(),key=lambda item:item[1],reverse=True))

        for val in sorted_dict.values():
            
            if val%2!=0:
                odd=max(odd,val)
            if val%2==0:
                even=max(even,val)
        diff=(odd-even)

        return(diff)

               