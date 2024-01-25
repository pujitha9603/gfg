#User function Template for python3

#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    # code here
	    mod = 10 ** 9 + 7
	    ans = [[1], [1, 1]]
	    for i in range(1, n + 1):
	        a = [1, 1]
	        b = ans[i]
	        for j in range(1, i + 1):
	            a.insert(j, (b[j] + b[j - 1]) % mod)
	        ans.append(a)
	    return ans[n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends