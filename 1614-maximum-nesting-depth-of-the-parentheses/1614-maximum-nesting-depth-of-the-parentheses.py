class Solution(object):
    def maxDepth(self, s):
        depth=0
        counter=0
        for i in s:
            if i=='(':
                counter+=1
                depth=max(counter,depth)
            if i==')':
                counter-=1

        return depth