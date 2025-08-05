class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        sz1=len(ransomNote)
        sz2=len(magazine)
        if sz1>sz2:
            return False
        t,p=0,0    
        while t < sz1 and p < len(magazine):
            if ransomNote[t]==magazine[p]:
                magazine = magazine[:p] + magazine[p+1:]
                t+=1
                p=0
            else:
                p+=1   
            if t==sz1:
                return True    
        return False            
                  
