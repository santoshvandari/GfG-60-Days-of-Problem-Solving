#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        res = 0
        n = len(arr)
        l = 0
        r = n-1
        while l<r:
            if arr[l]+arr[r]<target:
                l+=1
            elif arr[l]+arr[r]>target:
                r-=1
            else:
                c1=0
                c2=0
                e1=arr[l]
                e2=arr[r]
                
                while l<=r and arr[l]==e1:
                    l+=1
                    c1+=1
                while l<=r and arr[r]==e2:
                    r-=1
                    c2+=1
                if e1==e2:
                    res+=(c1*(c1-1))//2
                else:
                    res+=(c1*c2)
        return res
