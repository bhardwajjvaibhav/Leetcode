class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        numcandy=[]
        m =initialBoxes
        visited_b=[]
        visited_k=[]
        
        def status_check ():
            for i in m:
                if status[i]==1:
                    if i not in visited_b:
                        visited_b.append(i)
                        numcandy.append(candies[i])
                        key_check(i)
                        contain_check(i)
            
        def status_check2(p):
            if status[p]==1 and p not in visited_b:
                visited_b.append(p)
                numcandy.append(candies[p])
                key_check(p)
                contain_check(p)

        def key_check(a):
            
            for key in keys[a]:
                if key not in visited_k:
                    visited_k.append(key)
                    status[key]=1
                    status_check2(key) 
                
                
        def contain_check(n):
            
            for box in containedBoxes[n]:
                if box not in m :
                    m.append(box)
                    status_check2(box)
               
        status_check() 
        return sum(numcandy)