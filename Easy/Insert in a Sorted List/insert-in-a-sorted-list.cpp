//{ Driver Code Starts
//

#include <bits/stdc++.h> 
using namespace std; 

struct Node
{
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};


void printList(Node* node) 
{ 
	while (node != NULL) { 
		cout << node->data <<" "; 
		node = node->next; 
	}  
	cout<<"\n";
}

// } Driver Code Ends
/*
structure of the node of the list is as
struct Node
{
    int data;
    struct Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }
};
*/

class Solution{
  public:
    // Should return head of the modified linked list
    Node *sortedInsert(struct Node* head, int data) {
        // Code here
        // if(head == NULL){
        //     return new Node(data, head);
        // }
        // if(data <= head -> data){
        //     return new Node(data, head);
        // }
        // Node* temp = head;
        // while(temp -> next != NULL){
        //     if(temp -> next -> data > data){
        //         Node* x = new Node(data, temp -> next);
        //         temp -> next = x;
        //         break;
        //     }
        //     temp = temp -> next;
            
        // }
        // return head;
        
        Node* newNode = new Node(data);
        if(head == NULL || head -> data >= data){
            newNode -> next = head;
            return newNode;
        }
        Node* temp = head;
        Node* curr = head -> next;
        while(curr && curr -> data < data){
            temp = curr;
            curr = curr -> next;
        }
        temp -> next = newNode;
        newNode -> next = curr;
        return head;
    }
};


//{ Driver Code Starts.
int main() 
{ 
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
        
		int data;
		cin>>data;
		
		struct Node *head = new Node(data);
		struct Node *tail = head;
		for (int i = 0; i < n-1; ++i)
		{
			cin>>data;
			tail->next = new Node(data);
			tail = tail->next;
		}
		
		int k;
		cin>>k;
		Solution obj;
		head = obj.sortedInsert(head,k);
		printList(head); 
	}
	return 0; 
} 

// } Driver Code Ends