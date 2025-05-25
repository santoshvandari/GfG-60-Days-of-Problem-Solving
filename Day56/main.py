#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        s=0
        e=0
        res =[]
        curr= 0
        n=len(arr)
        for i in range(n):
            curr+=arr[i]
            if curr>=target:
                e=i
                while curr>target and s<e:
                    curr-=arr[s]
                    s+=1
                    
                if curr==target:
                    res.append(s+1)
                    res.append(e+1)
                    return res
        return [-1]
                