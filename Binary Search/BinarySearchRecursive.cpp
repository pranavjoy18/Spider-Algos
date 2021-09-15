#include <iostream>
using namespace std;

int BinarySearch(int arr,int low, int high,int key)
{

	if (low <= high)
	{

		int mid = (low + high)/2;

		if (arr[mid] == key)
			return mid;

		else if (arr[mid] > key)
			return BinarySearch(arr,low,mid-1,key);

		else
			return BinarySearch(arr,mid+1,high,key);

	}

	return -1;
}

int main()
{

	int T;
	cin>>T;

	while(T--)
	{

		int N,arr[100000],key;

		cin>>N;

		for (int i = 0; i < N; ++i)
			cin>>arr[i];

		cin>>key;

		cout<<BinarySearch(arr,0,N-1,key);
	}
}