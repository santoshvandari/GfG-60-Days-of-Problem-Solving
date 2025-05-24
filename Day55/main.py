#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        res = 0
        arr.sort()
        n=len(arr)
        
        for i in range(2,n):
            l,r=0,i-1
            while l<r:
                if arr[l]+arr[r]>arr[i]:
                    res+=r-l
                    r-=1
                else:
                    l+=1
        return res
                