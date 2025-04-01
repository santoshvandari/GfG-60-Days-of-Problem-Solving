#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr.sort(reverse=True)
        
        largest=arr[0]
        second_largest=-1
        for i in arr:
            if(largest>i):
                second_largest=i
                break
            
        return second_largest
                


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends