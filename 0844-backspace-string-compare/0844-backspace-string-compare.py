class Solution(object):
    def backspaceCompare(self, s, t):
        stack=[]
        dack=[]
        for i in s:
            if i=='#' and len(stack)>0:
                stack.pop()
            elif i!='#':
                stack.append(i)
        for i in t:
            if i=='#' and len(dack)>0:
                dack.pop()
            elif i!='#':
                dack.append(i)

        return stack==dack
        