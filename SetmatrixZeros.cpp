#include <iostream>
#include <vector>
using namespace std;

void setZeroes(vector<vector<int> > &A) {
vector<int> row;
vector<int> col;
int k=0,l=0;

for(int i=0; i<A.size();i++)
{
    for(int j=0; j< A[0].size();j++)
    {
        if(A[i][j]==0)
        {
            row.push_back(i);
            col.push_back(j);
        }   
    }
}
for(int i=0; i<row.size(); i++)
{
    int k=0,l=0;
    while(l<A.size()){
        A[l][col[i]]=0;
        l++;
    }
    while(k<A[0].size()){
        A[row[i]][k]=0;
        k++;
    }
}
	for (int i = 0; i < A.size(); i++) {
		for (int j = 0; j < A[0].size(); j++) {
			cout << A[i][j];
		}
		cout << endl;
	}
}

int main()
{
	std::vector<vector <int> > A;
	vector<int> v;
	v.push_back(0);
	A.push_back(v);
	setZeroes(A);
}