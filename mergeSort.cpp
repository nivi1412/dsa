#include <iostream>
#include <vector>

using namespace std;
void merge(std::vector<int> &v,int ls, int le, int rs, int re)
{
	int i=ls; int j=rs; std::vector<int> temp;
	while(i<=le && j<=re)
	{
		if(v[i] <= v[j])
		{
			temp.push_back(v[i]);
			i++;
		}
		else
		{
			temp.push_back(v[j]);
			j++;
		}
	}

	while(i<=le)
	{
		temp.push_back(v[i]);
		i++;
	}
	while(j<=re)
	{
		temp.push_back(v[j]);
		j++;
	}
	for(int k=0; k<temp.size(); k++)
	{
		v[ls+k]=temp[k];
	}
}
void mergesort(std::vector<int> &v,int s,int e)
{
	if (s==e){
		return; 
	}
	mergesort(v, s, (s+e)/2);
	mergesort(v, (s+e)/2+1, e);

	int ls=s;
	int le=(s+e)/2;
	int rs=(s+e)/2+1;
	int re=e;

	merge(v,ls,le,rs,re);

}
int main()
{
	std::vector<int> v;
	v.push_back(2);v.push_back(-1);v.push_back(-4);v.push_back(0);v.push_back(1);v.push_back(1);
	int start=0;
	int end=v.size()-1;

	mergesort(v, start,end);
	for(int i=0;i<v.size();i++)
	{
		cout<<v[i]<<endl;
	}
}

