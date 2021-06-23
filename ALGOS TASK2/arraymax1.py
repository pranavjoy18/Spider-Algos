''''Problem Statement:
You are given with an array of integers with size n , where a[i]=i. 
You will be given with q queries. 
In each query you have to add a value 'v' to each of the array element between the given indices (l,r) inclusive of both the indices. 
As a result, you have to return the maximum element of the resultant array after q operations.

Approach:
1.For every query looped over the list from l-1 to r index and added value to each element individually
2. Then returned the maximum value of the array after all operations
'''


def operations(arr,A):
    ''''This function takes an array of queries and the input array. Returns the input array after performing the query '''
    [l,r,val]=arr
    for i in range(l-1,r):
        A[i]+=val
    return A


if __name__=='__main__':
    N=int(input())#no of elements in array
    A=[i for i in range(1,N+1)]# assigning array as{1,2,3,4,5,...n}
    q=int(input())#no of queries
    Q=[]
    for i in range(q):
        Q.append([int(x) for x in input().split()])#accepting queries in a list Q
    
    for _ in Q:
        A=operations(_,A)#looping through Q performing every query on A
    print(max(A))#reurning out the maximum element in A after all the queries
    