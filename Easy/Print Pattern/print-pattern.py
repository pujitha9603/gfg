#User function Template for python3

class Solution:
    def pattern(self, N):
        # l = []
        # t = N
        # if t == 0:
        #     l.append(0)
        #     return l
        # l.append(t)
        # while t >= 0 and t != 0:
        #     t = t - 5
        #     l.append(t)
        # while t <= N:
        #     t = t + 5
        #     l.append(t)
        # return l[0 : len(l) - 1]
        arr = []
        num = N
        if num == 0:
            arr.append(0)
            return arr
        arr.append(num)
        while(num>=0 and num != 0):
            num = num-5
            arr.append(num)
        while(num<=N):
            num += 5
            arr.append(num)
        return arr[0:len(arr)-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends