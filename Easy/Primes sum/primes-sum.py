# User function Template for python3
class Solution:
    def isSumOfTwo (self, N):
        # code here 
    
        # p = [True] * (N + 1)
        # p[0] = False
        # p[1] = False
        # for i in range(2, (int(N ** 0.5)) + 1):
        #     if p[i]:
        #         for j in range(i + i, N + 1, i):
        #             p[j] = False
        # a = [i for i in range(2, N + 1) if p[i]]
        # i = 0
        # j = len(a) - 1
        # while(i <= j):
        #     if a[i] + a[j] > N:
        #         j -= 1
        #     elif a[i] + a[j] < N:
        #         i += 1
        #     else:
        #         return "Yes"
        # return "No"
        
        # if N < 4:
        #     return "No"
        # if N % 2 == 0:
        #     return "Yes"
        # else:
        #     a = []
        #     for i in range(1, N + 1):
        #         if prime(i):
        #             a.append(i)
        #     i = 0
        #     j = len(a) - 1
        #     while(i <= j):
        #         if a[i] + a[j] > N:
        #             j -= 1
        #         elif a[i] + a[j] < N:
        #             i += 1
        #         else:
        #             return "Yes"
        #     return "No"
        
        if N < 4:
            return "No"
        if N % 2 == 0:
            return "Yes"
        N -= 2
        for i in range(2, N + 1):
            if i * i <= N:
                if N % i == 0:
                    return "No"
        return "Yes"



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.isSumOfTwo(N))
# } Driver Code Ends