#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        k = N // 2
        d = {}
        for i in A:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i, j in d.items():
            if j > k:
                return i
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends