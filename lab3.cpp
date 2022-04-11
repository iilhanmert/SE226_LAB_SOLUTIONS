#include <iostream>
using namespace std;
#define Max 1000



class Node {
public:
    int data;
    Node *next;

    Node(int data)
    {
        this ->data=data;
        next=NULL;
    }
};

class Stack {

public:
    Node *top;
    int s ;
    Stack()
    {
        top==NULL;
    }
    bool push(int);

    bool isEmpty();

    int pop();

    int peek();
};
bool Stack:: push(int data)
{


    Node *n=new Node(data);
    if(top==NULL)
        top=n;
    else{
        n->next=top;
        top=n;
    }}

int Stack :: pop() {
    Node *temp;
    if (top == NULL) {
        cout << "\nStack Underflow" << endl;
        return -1;
    } else {

        int tempData=top->data;
        Node *temp=top;
        top=top->next;
        int tmp;

        int tmpData;
        return tmpData;}
};



bool Stack ::isEmpty() {

    return top == NULL;
}


int Stack :: peek() {

    if (!isEmpty())
        return top->data;
    else
        exit(1);
};




int main()
{
    class Stack s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);



    cout << "\nTop element is "<< s.peek() << endl;


    s.pop();
    s.pop();



    cout << "\nTop element is "<< s.peek() << endl;

    return 0;
}