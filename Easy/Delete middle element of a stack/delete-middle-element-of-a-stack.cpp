//{ Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++

class Solution
{
    public:
    //Function to delete middle element of a stack.
    
    void deleteEle(stack<int>&s, int c, int len){
        if(c == (len / 2) + 1){
            s.pop();
        }
        else{
            int n = s.top();
            s.pop();
            deleteEle(s, c + 1, len);
            s.push(n);
        }
    }
    
    
    void deleteMid(stack<int>&s, int sizeOfStack)
    {
        // code here.. 
        deleteEle(s, 1, sizeOfStack);
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin>>t;
    
    while(t--)
    {
        int sizeOfStack;
        cin>>sizeOfStack;
        
        stack<int> myStack;
        
        for(int i=0;i<sizeOfStack;i++)
        {
            int x;
            cin>>x;
            myStack.push(x);    
        }

            Solution ob;
            ob.deleteMid(myStack,myStack.size());
            while(!myStack.empty())
            {
                cout<<myStack.top()<<" ";
                myStack.pop();
            }
        cout<<endl;
    }   
    return 0;
}

// } Driver Code Ends