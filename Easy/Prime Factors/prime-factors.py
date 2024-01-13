#User function Template for python3

class Solution:
	def AllPrimeFactors(self, N):
		# Code here
		def prime(n):
		    if n<= 1:
		        return 0
		    for i in range(2, (int(n ** 0.5)) + 1):
		        if n % i == 0:
		            return 0
		    return 1
		l = []
		for i in range(1 , N+1):
		    if N % i == 0 and prime(i):
		        l.append(i)
		return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends