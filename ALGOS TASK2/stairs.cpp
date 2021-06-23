/*Problem Statement:
Anuj has to climb up stairs to reach the first floor of his home. He can either climb up one step or two steps at a time. 
However there is a catch. There are some stairs that are not safe to step on. 
You have to count the number of ways that Anuj can reach the nth stair. 
He is initially on the ground floor, i.e. 0th step. 
Since the number of ways can be a large number, find the count modulo 1000000007.

Approach:
It has been observed that the ways to reach the nth step depends :
ways[n]=ways[n-1]+ways[n-2]

But, since he cannot step on a broken step,ways[broken_step]=0

1.We initialise an array ways[] of size n+1(n is no of stairs) to store the number of ways to reach the ith step from 0-n+1
2.There is only one way to reach the 0th step so ways[0]=0
3.Depending upon whether the first step is broken or not we assign ways[1]=1(if not broken) or ways[1]=0 otherwise
4.For the rest of the elements , if the stair is broken we store 0 else we store the sum of the previous two elements
5.Return the last element of array 



*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,m;
    cin >>n>>m;
    int broken[m];//array to store the steps which are broken
    int ways[n+1];//array to store the no of ways of reaching each step 
    for(int i=0;i<m;i++)
    cin >>broken[i];
    ways[0]=1;
    if(m!=0)//if atleast one step is broken then not required to loop over broken[] array
    {
    if(broken[0]==1)//if the first step is broken then zero ways to reach it
    {
        ways[1]=0;
        int k=1;//an integer k which would act as index element for array broken[]
     for(int i=2;i<=n;i++)
     {
         if(i==broken[k])//if a stair is broken assign ways[i]=0
         {
             ways[i]=0;
             k++;//increment the index in broken[] array if a broken stair has been found
         }
         else
             ways[i]=(ways[i-1]+ways[i-2])%1000000007;//modulo to report the answer in specified format
     }
    }
    else
    {
    ways[1]=1;//ways[1]=1 when the 1st step is not broken
    int k=0;
    for(int i=2;i<=n;i++)
    {
        if(i==broken[k])
        {
            ways[i]=0;
            k++;
        }
        else
        ways[i]=(ways[i-1]+ways[i-2])%1000000007;
    }
    }
    }
    else
    {   //if none of steps are broken dont need to loop over the broken[] array
        ways[1]=1;
        for(int i=2;i<=n;i++)
          ways[i]=(ways[i-1]+ways[i-2])%1000000007;
    }
    cout<<ways[n];
    return 0;
}
