class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
       #for path in paths:
       notAns = set() 
       for a,b in paths:
           notAns.add(a)

       for a,b in paths:
            if b not in notAns:
                return b