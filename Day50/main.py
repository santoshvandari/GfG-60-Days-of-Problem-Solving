class Solution:
    def subarrayXor(self, arr, k):
        # code here
        res = 0
        mp = {
        
        }
        
        prefxor = 0
        
        for value in arr:
            prefxor ^=value
            res+=mp.get(prefxor^k,0)
            if prefxor==k:
                res+=1
            mp[prefxor]=mp.get(prefxor,0)+1
        return res

            
        
        
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends