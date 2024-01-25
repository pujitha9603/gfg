//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends
class Solution{
public:
    bool happynum(int n){
        if( n == 1 || n == 7){
            return true;
        }
        else if(n ==  2 || n == 3 || n == 4 || n == 5 || n == 6 || n == 8 || n == 9){
            return false;
        }
        int sqsum = 0;
        while(n){
            int d = n % 10;
            sqsum += (d * d);
            n = n / 10;
        }
        return happynum(sqsum);
    }
    
    int nextHappy(int N){
        // code here
        while(true){
            N++;
            if(happynum(N)){
                return N;
            }
        }
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.nextHappy(N) << endl;
    }
    return 0; 
}
// } Driver Code Ends