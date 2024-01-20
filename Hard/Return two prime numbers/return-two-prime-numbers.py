#User function Template for python3

class Solution:
    def primeDivision(self, N):
        # code here
        def prime(n):
            if n <= 1:
                return False
            for i in range(2, (int(n ** 0.5)) + 1):
                if n % i == 0:
                    return False
            return True
        l = []
        if N == 4:
            return (2, 2)
        for i in range(N - 1, 0, -2):
            if prime(N - i) and prime(i):
                return (N- i, i)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends