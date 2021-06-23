
/*Problem Statement: 
There exist an integer array A of length N whose values are unknown to us. 
We are given an integer sequence B of length N−1 as input. 
We also know that : Bi≥max(Ai,Ai+1) (i.e., every value of B array at ith index ,will be greater than values at Ai and Ai+1 , for every i from 0 to N-1).
Find the maximum possible sum of the elements of A.

Approach:

Let us take the array B and make the array A out of it:

given that Bi>=max(Ai,Ai+1)
So,
B[0]>=max(A[0],A[1])
so for maximum possible sum we can say that A[0]=A[1]=B[0]
since we are using only one array , we make the following transformation in array B:
B[0]=B[1]

Now our array B={B[0],B[0],B[2]....B[n-1]}
now since we have only one array to represent both A and B :
we can now alter the conditions:
B[i]>=max(B[i],B[i+1])
so ,
if B[i]<B[i-1], max(B[i],B[i-1])=B[i-1]
so we need to make : B[i-1]=B[i]
so now B[i]=max(B[i],B[i])=B[i]

ex:B[1]=3,B[2]=2
now B[1]=2
max(B[1],B[2])=2=B[1]

Then we sum up the array to get the maximum sum

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,arr[101];
  cin>>n;
  for (int i=1;i<n;++i)
  cin>>arr[i];

  arr[0]=arr[1];
  for (int i=1;i<n;i++)
  if (arr[i-1]>arr[i])
  arr[i-1]=arr[i];

  int sum=0;
  for(int i=0;i<n;i++)
  sum+=arr[i];

  cout<<sum;
    
    return 0;
}
