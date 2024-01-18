#User function Template for python3

class Solution:
    def jugglerSequence(self, N):
        l = [N]
        while N != 1:
            if N % 2 == 0:
                N = int(N ** (1/2))
            else:
                N = int(N ** (3/2))
            l.append(N)
        return l
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.jugglerSequence(N)
        for i in (arr):
            print(i,end=" ")
        print()
# } Driver Code Ends