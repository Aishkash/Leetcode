class Solution(object):
    def generate(self, numRows):
        ans=[]
        k=[1,1]
        for i in range(1, numRows+1):
            a=[1]*i
            for j in range(1,i-1):
                a[j]=k[j-1]+k[j]
            k=a
            ans.append(a)
        return ans