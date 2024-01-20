#User function Template for python3

class Solution:
    def getLastDigit(self, a, b):
        # code here 
        x = int(a)
        y = int(b)
        if y == 0:
            return 1
        r = y % 4
        if r == 0:
            return (x ** 4) % 10
        return (x ** r) % 10

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(str,input().split())
        
        ob = Solution()
        print(ob.getLastDigit(a,b))
# } Driver Code Ends