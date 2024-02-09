class Solution:
    def duplicates(self, arr, n):
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = []
        for i, j in d.items():
            if j > 1:
                l.append(i)
        if len(l) == 0:
            return [-1]
        else:
            return sorted(l)
    	# code here
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends