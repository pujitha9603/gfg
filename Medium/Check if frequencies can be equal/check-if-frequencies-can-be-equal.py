#User function Template for python3
class Solution:
    def sameFreq(self, s):
        # code here
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        f = list(d.values())
        # l = sorted(list(set(f)))
        # if len(l) == 1:
        #     return 1
        # elif len(l) == 2:
        #     a = l[0] - 1
        #     if a == 0 or a == l[-1]:
        #         return 1
        #     else:
        #         return 0
        # else:
        #     return 0
        if len(set(f)) == 1:
            return 1
        else:
            for i in range(len(f)):
                f[i] = f[i] - 1
                if len(set(f)) == 1 or (f[i] == 0 and len(set(f)) == 2):
                    return 1
                f[i] = f[i] + 1
            else:
                return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends