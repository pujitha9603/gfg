#User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
        ans = sorted(array1 + array2)
        ind = len(ans) // 2
        if len(ans) % 2 != 0:
            return ans[ind]
        else:
            a = ans[ind] + ans[ind - 1]
            if a % 2 == 0:
                return a // 2
            else:
                return a / 2


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends