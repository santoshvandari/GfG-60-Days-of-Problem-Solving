class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        res = []
        freq = {}
        
        for i in range(k):
            if arr[i] in freq:
                freq[arr[i]]+=1
            else:
                freq[arr[i]]=1
        res.append(len(freq))
        for i in range(k,n):
            if arr[i] in freq:
                freq[arr[i]]+=1
            else:
                freq[arr[i]]=1
            
            temp = arr[i-k]
            freq[temp]-=1
            
            if freq[temp]==0:
                del freq[arr[i-k]]
            res.append(len(freq))
        return res