#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        prefix_sum = {}
        result = 0
        current_sum = 0
        for value in arr:
            current_sum = current_sum + value
            if current_sum == k:
                result  = result +1
            if current_sum -k in prefix_sum:
                result+=prefix_sum[current_sum-k]
            prefix_sum[current_sum]=prefix_sum.get(current_sum,0)+1
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends