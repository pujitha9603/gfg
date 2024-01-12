#User function Template for python3
class Solution:
	def primeSetBits(self, L, R):
		# code here
		def prime(n):
            if n <= 1:
                return False
            for i in range(2, (int(n ** 0.5)) + 1):
                if n % i == 0:
                    return False
            return True
        def set_count(n):
            if n == 0:
                return 0
            elif n & 1 == 1:
                return 1 + set_count(n // 2)
            else:
                return set_count(n // 2)
        c = 0
        for i in range(L, R + 1):
            if prime(set_count(i)):
                c += 1
        return c
		    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		L,R = input().split()
		L=int(L)
		R=int(R)
		ob = Solution();
		print(ob.primeSetBits(L,R))

# } Driver Code Ends