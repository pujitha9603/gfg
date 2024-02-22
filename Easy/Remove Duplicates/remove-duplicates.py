#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		d = {}
		for i in range(len(S)):
		    if S[i] not in d:
		        d[S[i]] = i
	    l = []
	    for i, j in d.items():
	        l.append([j, i])
	    f = sorted(l)
	    s = ""
	    for i in range(len(f)):
	        s += f[i][1]
	    return s
		 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends