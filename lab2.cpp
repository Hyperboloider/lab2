#include <iostream>
using namespace std;

int main()
{   
    float a, b, c, d, Div1, Div2, Div3, Div4;
    int res;
    cin>>a>>b>>c>>d;
    Div1 = a/c;
    Div2 = b/d;
    Div3 = a/d;
    Div4 = b/c;
    
    if (Div1 == Div2) { 
        res = 1;} 
        else { 
            if (Div3==Div4) {     
             res = 1;} 
                else { res = 0;}}
    cout<< res;
    return 0;
}            