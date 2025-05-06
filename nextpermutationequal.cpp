#include <iostream>
#include <vector>
using namespace std;


void reverse(vector <int> &A)
{
    for (int i=0;i<A.size()/2;++i)
    {
        int temp;
        temp=A[i];
        A[i]=A[A.size()-i-1];
        A[A.size()-i-1]=temp;
    }

}

int minimum (vector<int> &A)
{    
    int small=A[0];
    for(int i=1; i<A.size();i++)
    {
        if(small > A[i])
        {
            small = A[i];
        }
    }
    return small;
}


 void nextPermutation(vector<int> &A) 
 {
    int size = A.size();
    int aend;
    int dstart=-1;

    if(A[size-1] > A[size-2]) //If Ascending non repeating then swap last 2 digits
    {
        int swap;
        swap=A[size-1];
        A[size-1]=A[size-2];
        A[size-2]=swap;

        for (int i =0; i< A.size();i++)
        {
            cout<<A[i]<<endl;
        }
        cout<<"Ascending"<<endl;
        return;
    }

    for(int i=A.size()-1; i>0; i--)
    {
        if(A[i] < A[i-1])
        {
        }
        else
        {
            dstart=i;
            break;
        }
    }
    if (dstart==-1) // this is the condition where array is in descending order and non repeating(sort the array)
    {
        reverse(A);
        for (int i =0; i< A.size();i++)
        {
            cout<<A[i]<<endl;
        }
        cout<<"Descending"<<endl;
        return;
    }
    else // if the array is in Ascending start and have a descending end (the least value of the descending end array should be > the ascending array end elment)
    { // find the least value from dtart to A.size which is > aend
        
        aend = dstart-1;
        int small = A[dstart];
        int small_index;
        int tempswap;
        cout << "dstart " << dstart << endl;

        for(int i= dstart+1; i<size; i++)
        {    
            cout<<i << " " << A[i]<<endl;
            if(small > A[i] && A[i] > A[aend])
            {
                //cout<<A[i]<<endl;
                small=A[i];
                small_index=i;
            }
        }
//Swap small_index with the aend
        tempswap=A[small_index];
        A[small_index]=A[aend];
        A[aend]=tempswap;

        cout<< "small_index" << A[small_index] <<" "<< "aend"<< A[aend] <<endl;

        sort(A.begin()+dstart,A.end());
    }

    for (int i =0; i< A.size();i++)
    {
        cout<<A[i]<<endl;
    }

    cout<<"Ascendingandescending";
    return;
}

int main()
{
    vector<int> A;
    A.push_back(1);
    A.push_back(6);
    A.push_back(5);
    A.push_back(4);
    A.push_back(3);
    A.push_back(2);
    nextPermutation(A);
}