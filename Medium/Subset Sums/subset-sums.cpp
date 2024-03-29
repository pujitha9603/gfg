//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
class Solution
{
public:
    
    void fun(int i, int N, vector<int> &arr, vector<int> &v, int s){
        if(i == arr.size()){
            v.push_back(s);
            return;
        }
        fun(i + 1, N, arr, v, s + arr[i]);
        fun(i+1, N, arr, v, s);
    }

    vector<int> subsetSums(vector<int> arr, int N)
    {
        // Write Your Code here
        vector<int> v;
        int s;
        fun(0, N, arr, v, s);
        sort(v.begin(), v.end());
        return v;
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        vector<int> arr(N);
        for(int i = 0 ; i < N ; i++){
            cin >> arr[i];
        }
        Solution ob;
        vector<int> ans = ob.subsetSums(arr,N);
        sort(ans.begin(),ans.end());
        for(auto sum : ans){
            cout<< sum<<" ";
        }
        cout<<endl;
    }
    return 0;
}
// } Driver Code Ends