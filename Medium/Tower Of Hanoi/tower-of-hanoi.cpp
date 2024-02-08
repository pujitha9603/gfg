//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
class Solution{
    public:
    // You need to complete this function

    // avoid space at the starting of the string in "move disk....."
    long long toh(int N, int s, int to, int h) {
        // Your code here
        if(N == 0){
            return 0;
        }
        else if(N == 1){
            cout << "move disk 1 from rod " << s << " to rod " << to << endl;
            return 1;
        }
        else{
            int c = 0;
            c += toh(N -1, s, h, to);
            cout << "move disk " << N << " from rod " << s << " to rod " << to << endl;
            c++;
            c += toh(N - 1, h, to, s);
            return c;
        }
    }

};

//{ Driver Code Starts.

int main() {

    int T;
    cin >> T;//testcases
    while (T--) {
        
        int N;
        cin >> N;//taking input N
        
        //calling toh() function
        Solution ob;
        
        cout << ob.toh(N, 1, 3, 2) << endl;
    }
    return 0;
}



// } Driver Code Ends