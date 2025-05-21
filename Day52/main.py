#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        n = len(arr)
        l,r=0,n-1
        count = 0
        
        while(l<r):
            sum = arr[l]+arr[r]
            if sum<target:
                count +=r-l
                l+=1
            else:
                r-=1
        return count