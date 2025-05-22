#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        n = len(arr)
        arr.sort()
        res = []
        left = 0
        right = n -1
        
        mindiff = float('inf')
        while left<right:
            cursum = arr[left]+arr[right]
            if abs(target-cursum)<mindiff:
                mindiff = abs(target - cursum)
                res = [arr[left],arr[right]]
            if cursum < target:
                left+=1
            elif cursum>target:
                right -=1
            else:
                return res
        return res
        