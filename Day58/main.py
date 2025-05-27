#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        n = len(s)
        res = 0
        lIdx = [-1] *26
        start = 0
        
        for end in range(n):
            start = max(start,lIdx[ord(s[end])-ord('a')]+1)
            res = max(res,end-start+1)
            lIdx[ord(s[end])-ord('a')]=end
        return res