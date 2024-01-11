#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here
    	p = [True] * (N + 1)
    	p[0] = False
    	p[1] = False
    	for i in range(2, int(N ** 0.5) + 1):
    	    if p[i]:
    	        for j in range(i + i , N + 1, i):
    	            p[j] = False
        return [i for i in range(2, N + 1) if p[i]]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends