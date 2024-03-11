#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
		# code here
# 		r = len(mat1)
# 		c = len(mat1[0])
# 		a = []
# 		b = []
# 		cnt = 0
# 		for i in range(r):
# 		    for j in range(c):
# 		        a.append(mat1[i][j])
# 		        b.append(mat2[i][j])
# 		for i in a:
# 		    if x - i in b:
# 		        cnt += 1
# 		return cnt

        c=0
        i=0
        j=0
        p=n-1
        q=n-1
	    while i<=n-1 and p>=0:
	        if mat1[i][j]+mat2[p][q]==x:
	            c+=1
	            j+=1
	            if j>n-1:
	                i+=1
	                j=0
	            q-=1
	            if q<0:
	                p-=1
	                q=n-1
	        elif mat1[i][j]+mat2[p][q]<x:
	            j+=1
	            if j>n-1:
	                i+=1
	                j=0
	        elif mat1[i][j]+mat2[p][q]>x:
	            q-=1
	            if q<0:
	                p-=1
	                q=n-1
        return c




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends