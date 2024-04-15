#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):

        # code here
        lst = []
        b.sort()
        for i in range(q):
            qi = query[i]
            ai = a[qi]
            c = 0
            l = 0
            r = len(b) - 1
            while l <= r:
                m = (l + r) // 2
                if b[m] <= ai:
                    l = m + 1
                else:
                    r = m - 1
            lst.append(l)
            
        return lst
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends