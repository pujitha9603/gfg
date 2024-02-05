#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        m = 0
        for i in range(0, len(S1) -1):
            for j in range(i, len(S1)):
                a = S1[i:j+1]
                if a in S2:
                    c = len(a)
                    m = max(m, c)
        return m
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends