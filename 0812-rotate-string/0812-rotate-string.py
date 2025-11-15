class Solution(object):
    def rotateString(self, s, goal):
        a=len(s)
        b=len(goal)
        if a!=b:
            return False
        return goal in (s + s)
            
        