#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends

#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        # Your code here
        map = {}
        ans  = []
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                value = -1 * (arr[i]+arr[j])
                if value in map:
                    for k in map[value]:
                        ans.append([k,i,j])
            if arr[i] not in map:
                map[arr[i]] = []
            map[arr[i]].append(i)
        return ans
        


#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends