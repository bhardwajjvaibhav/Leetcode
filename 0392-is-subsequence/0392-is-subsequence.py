class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pt_s=0
        pt_t=0

        while pt_t<len(t):
            if pt_s<len(s) and s[pt_s]==t[pt_t]:
                pt_s+=1

            pt_t+=1

        return pt_s==len(s)