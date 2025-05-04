#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        n = len(arr)
        newArr = set(arr)
        
        count = 0
        curr = 0
        while count < k:
            curr = curr + 1
            if curr not in newArr:
                count += 1
        return curr
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends