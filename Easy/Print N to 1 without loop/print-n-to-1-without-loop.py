#User function Template for python3

class Solution:
    def printNos(self, n):
        # Code here
        def fun(N):
            if N >= 1:
                return N
        for i in range(n, 0, -1):
            print(fun(i), end = " ")
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
# } Driver Code Ends