#include <iostream>
using namespace std; 

void insertionsort(int arr[],int size)
{
	for(int i=1;i<size;i++)
	{

      int j =i-1;
      int key=arr[i];
      while(arr[j]>key && j>=0)
      {
      	arr[j+1]=arr[j];
      	j=j-1;
      }
      arr[j+1]=key;
	}
}

int main()
{
	int arr[]={13, 2 , 5, 15, 7 ,18, 1};
	int size=sizeof(arr)/sizeof(arr[0]);
	insertionsort(arr,size);
	for (int i=0;i<size;i++)
	{
		cout<<"final sorted array:"<<arr[i]<<"\n";
	}
	return 0;
}