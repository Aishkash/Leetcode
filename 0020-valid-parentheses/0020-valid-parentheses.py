class Solution(object):
    def isValid(self, s):
        sz=len(s)
        a=[]
        for i in s:
            l=len(a)
            if l>0 and a[-1]=='(' and i==')':
                a.pop()
            elif l>0 and a[-1]=='{' and i=='}':
                a.pop()
            elif l>0 and a[-1]=='[' and i==']':
                a.pop()
            else:
                a.append(i)       

        return len(a)==0
       