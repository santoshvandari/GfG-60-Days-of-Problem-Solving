
class Solution:
    def maxWater(self, arr):
        # code here
        st = []
        res = 0
        n = len(arr)
        
        for i in range(n):
            
            while st and arr[st[-1]]<arr[i]:
                height = arr[st.pop()]
                
                if not st:
                    break
                
                distance = i-st[-1] -1
                
                water = min(arr[st[-1]],arr[i])
                
                water -=height
                
                res += distance * water
            
            st.append(i)
        
        return res