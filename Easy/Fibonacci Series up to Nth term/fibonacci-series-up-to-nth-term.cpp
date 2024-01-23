//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    vector<long long> Series(int N) {
        // COde here
        vector<long long>fibseq;
        if(N == 0 || N == 1){
            fibseq.push_back(0);
            fibseq.push_back(1);
        }
        else{
            fibseq = Series(N - 1);
            fibseq.push_back(fibseq[N - 1] + fibseq[N - 2]);
        }
        return fibseq;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution obj;

        vector<long long> ans = obj.Series(n);
        for (auto x : ans) cout << x << " ";
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends