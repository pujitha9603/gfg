#User function Template for python3
class Solution:
    def leastPrimeFactor (self, n):
        least_pf = [0] * (n + 1)
        least_pf[1] = 1
        for i in range(2, n + 1):
            if least_pf[i] == 0:
                least_pf[i] = i
                for j in range(i * i, n + 1, i):
                    if least_pf[j] == 0:
                        least_pf[j] = i
        return least_pf
                    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends