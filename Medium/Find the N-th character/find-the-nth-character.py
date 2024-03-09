#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        # ans = ""
        # if r % 2 == 0:
        #     for i in s:
        #         if i == "1":
        #             ans += "1" + "0" * r + "1"
        #         else:
        #             ans += "0" + "1" * r + "0"
        #     return ans[n]
        # else:
        #     for i in s:
        #         if i == "1":
        #             ans += "1" + "0" * r
        #         else:
        #             ans += "0" + "1" * r
        #     return ans[n]
            
        def fun(s,c,r):
            if c >= r:
                return s
            t = ""
            for i in s:
                if i=="0":
                    t += "01"
                else:
                    t += "10"
            c += 1
            return fun(t,c,r)   
        c = 0
        on = "1"
        tw = "0"
        ones  = fun(on,c,r)
        twos = fun(tw,c,r)
        t = ""
        for i in s:
            if i == "1":
                t += ones
            else:
                t += twos 
            if len(t)>n:
                return t[n]
        return t[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends