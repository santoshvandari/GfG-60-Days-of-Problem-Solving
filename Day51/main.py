
class Solution:
    def countTriplets(self, arr, target):
        # code here
        n = len(arr)
        res = 0
        for i in range(n-2):
            l = i+1
            r = n-1
            while l<r:
                sum = arr[i] + arr[l] + arr[r]
                if sum < target:
                    l = l+1
                elif sum > target:
                    r -=1
                else:
                    el1=arr[l]
                    el2=arr[r]
                    c1=0
                    c2=0
                    while l<=r and arr[l]==el1:
                        l=l+1
                        c1+=1
                    while l<=r and arr[r]==el2:
                        r-=1
                        c2+=1
                    if el1==el2:
                        res+=(c1*(c1-1)) // 2
                    else:
                        res+=(c1*c2)
        return res
                    
                    
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends