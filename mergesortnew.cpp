#include <iostream>

void merge(int arr[],int p, int q, int r)
{ 
	int i=0;int j=0;int left[100]=0;int right[100]=0;
	
	while(i<=q)
	{
      left[i]=arr[i];
      i++;
	}
	while(j<=r)
	{
	  right[j]=arr[j];
	  j++;
	}
    
    i=0;j=0;int k=0;

    while(i<=q and j<=r)
    {
    	if(left[i]>right[j])
    	{
          arr[k]=right[j];
          j++;k++;
    	}
    	if(left[i]<right[j])
    	{
    	  arr[k]=left[i];
    	  i++;k++;
    	}
    }

    while(i<=q)
    {
    	arr[k]=left[i];
    	k++;
    	i++;
    }
    while(j<=r)
    {
    	arr[k]=right[j];
    	k++;
    	j++;
    }

}


void mergesort(int arr[] ,int p, int r)
{
	if (p>=r)
		return
	else
		int q = (p+r/2);
	mergesort(&arr,p,q);
	mergesort(&arr,q+1,r);
	merge(&arr,p,q,r);
}


int main()
{
	int arr = {'60','50','40','30','20','10'};
	int size=sizeof(arr)/size(arr[0]);
	int p=1; int r=size;
	mergesort(&arr,p,r)
	return 0;
}