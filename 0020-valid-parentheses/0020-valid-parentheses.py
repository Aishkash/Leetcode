class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            l=len(stack)
            if l>0 and stack[-1]=='{' and i=='}':
                stack.pop()
            elif l>0 and stack[-1]=='[' and i==']':
                stack.pop()
            elif l>0 and stack[-1]=='(' and i==')':
                stack.pop()
            else:
                stack.append(i)
        l=len(stack)
        return l==0
        