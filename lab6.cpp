#include <iostream>
#include <string>
using namespace std;

double var = 0;
double multip = 1;


double myFunc(double n ){
    var = n;
    var = (var / (var + 2)) - 10;
    multip = multip*var;
    if  (n==1){
        cout<< "Multiplication Result: " << multip << endl;
        return multip;
    }
    else{
        cout<<multip<<endl;
        return myFunc(n-1);
    }
}

double myFunc(){
    double n;
    cout<<"Please enter n value for overloaded function : "<< endl;
    cin>>n;

    for (double i = n; i ==1 ; i--) {
        var = n;
        var = (var / (var + 2)) - 10;
        multip = multip * var;
        cout<<"Multiplication Result At Every Step: " << multip << endl; // i can not print out this line idk why?
    }
    return multip;
}

int main() {

    int userNum;
    cout<<"Please enter n value: "<<endl;
    cin>>userNum;
    cout<<myFunc(userNum)<<endl;

    cout<<myFunc()<<endl;

    return 0;
}