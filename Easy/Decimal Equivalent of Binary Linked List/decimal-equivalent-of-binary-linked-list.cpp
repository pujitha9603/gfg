//{ Driver Code Starts
// Program to check if linked list is empty or not
#include<iostream>
using namespace std;
const long long unsigned int MOD = 1000000007;

/* Link list Node */
struct Node
{
    bool data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
};


// } Driver Code Ends
/* Below global variable is declared in code for modulo arithmetic
const long long unsigned int MOD = 1000000007; */

/* Link list Node/
struct Node
{
    bool data;   // NOTE data is bool
    Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
}; */

// class Solution
// {
//     public:
//         // Should return decimal equivalent modulo 1000000007 of binary linked list
        
//         long long unsigned int decimalValue(Node *head)
//         {
//           // Your Code Here
//           int n = 0;
//           Node* temp = head;
//           while(temp){
//               n++;
//               temp = temp -> next;
//           }
           
//           long long m = 1000000007;
//           int c = 1;
//           long long sum = 0;
//           temp = head;
//           while(temp){
//               sum = sum + ((temp -> data) * pow(2, n - c)) % m;
//               c++;
//               temp = temp -> next;
//           }
//           return sum % m;
           
//         }
// };

class Solution
{
    public:
        // Should return decimal equivalent modulo 1000000007 of binary linked list 
        long long unsigned int decimalValue(Node *head)
                {
          int mod=1e9+7;
          long long unsigned int ans=0;
          Node* prev=NULL;
          while(head){
              Node* next=head->next;
              head->next=prev;
              prev=head;
              head=next;
          }
          long long unsigned int pow=1;
          while(prev){
              if(prev->data) ans=(ans+pow)%mod;
              pow=(pow*2)%mod;
              prev=prev->next;
          }
          return ans%mod;
        }
};




//{ Driver Code Starts.

void append(struct Node** head_ref, struct Node **tail_ref, bool new_data)
{

    struct Node* new_node = new Node(new_data);
    
    if (*head_ref == NULL)
       *head_ref = new_node;
    else
       (*tail_ref)->next = new_node;
    *tail_ref = new_node;
}


bool isEmpty(struct Node *head);

/* Driver program to test above function*/
int main()
{
    bool l;
    int i, n, T;

    cin>>T;

    while(T--){
    struct Node *head = NULL,  *tail = NULL;

        cin>>n;
        for(i=1;i<=n;i++)
        {
            cin>>l;
            append(&head, &tail, l);
        }
        Solution obj;
        cout << obj.decimalValue(head) << endl;
    }
    return 0;
}
// } Driver Code Ends