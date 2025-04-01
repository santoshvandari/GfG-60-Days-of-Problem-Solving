#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        arr_len=len(arr)
        temp=[0]*arr_len
        index = 0
        for i in arr:
            if i !=0:
                temp[index]=i
                index+=1
    	   # if i==0:
    	        
        for i in range(0,arr_len):
    	    arr[i]=temp[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
        print("~")
# } Driver Code Ends