class Solution(object):
    def backspaceCompare(self, s, t):
        sz=len(s)
        i=sz-1
        k=0
        new=''
        while i>-1:
            if s[i]=='#':
                k+=1
                i-=1
            else:
                if k>0:
                    while i >= 0 and k > 0:
                        if s[i] == '#':
                            k += 1
                        else:
                            k -= 1
                        i -= 1
                else:
                    new+= s[i]
                    i-=1        
        szz=len(t)
        i=szz-1
        k=0
        new2=''
        while i>-1:
            if t[i]=='#':
                k+=1
                i-=1
            else:
                if k>0:
                    while i >= 0 and k > 0:
                        if t[i] == '#':
                            k += 1
                        else:
                            k -= 1
                        i -= 1
                else:
                    new2+= t[i]
                    i-=1
        return new==new2