#include<iostream>
using namespace std;

bool BinarySearch(int N , int arr[], int key)
{

	int low = 0;
	int high = N-1;

	while (low <= high)
	{

		
		int mid = (low + high)/2;
		

		if(arr[mid] == key)
			return true;

		else if (key < arr[mid])
			high = mid -1;

		else
			low = mid +1;
	}

	return false;
} 

int main()
{

	int T;
	cin>>T;

	while(T--)
	{

		int N,arr[1000000],key;

		cin>>N;

		for(int i = 0;i < N;i++)
			cin>>arr[i];

		cin>>key;

		cout<<BinarySearch(N,arr,key)<<endl;
	}

	return 0;
}	