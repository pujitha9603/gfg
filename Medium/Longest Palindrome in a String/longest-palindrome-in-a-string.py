#User function Template for python3

class Solution:
    def longestPalin(self, S):
        
        # code here
        if S == S[::-1]:
            return S
        m = 0
        l = []
        for i in range(0, len(S) - 1):
            for j in range(i, len(S)):
                a = S[i:j+1]
                rev_a = a[::-1]
                if a == rev_a:
                    l.append(rev_a)
                    c = len(rev_a)
                    m = max(m, c)
        for i in l:
            if len(i) == m:
                return i
 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends