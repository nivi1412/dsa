#include <iostream>
#include <vector>
using namespace std;



void solve(vector<int> &A) {
    int count=0;
    for (int i=0; i<A.size();i++)
    {
        if(A[i]<0)
        {
            count++;
            A[i]=A[i]*-1;
        }
    }
    
    vector<int> C;
    vector<int> B;
    vector <int> out;
    int flag1,flag2;
    
    for(int i=0; i< count;i++)
    {
        C.push_back(A[i]);
        cout<<C[i];
    }
    for (int j=count; j< A.size(); j++)
    {
        B.push_back(A[j]);
        cout<<B[j+count];
    }
    cout << endl;

    int i=0, j=C.size()-1;
    while(i<B.size()&&j>=0)
    {
        if(B[i]>=C[j])
        {
            out.push_back(C[j]*C[j]);
            j--;    

        }
        else
        {
            out.push_back(B[i]*B[i]);
            i++;
        }
    }
    while(i<B.size())
    {
    out.push_back(B[i]*B[i]);
    i++;
    }
    while(j>=0)
    {
    out.push_back(C[j]*C[j]);
    j--;
    }


for (int i=0; i< out.size();i++)
{
    cout << out[i] <<endl;
}
}

int main()
{
    std::vector<int> A;
    A.push_back(-8);
    A.push_back(-6);
    A.push_back(-5);
    A.push_back(0);
    A.push_back(1);
    A.push_back(6);
    solve(A);
}
