'''Problem Statement:
You are given with an array of integers with size n , where a[i]=i. 
You will be given with q queries. 
In each query you have to add a value 'v' to each of the array element between the given indices (l,r) inclusive of both the indices. 
As a result, you have to return the maximum element of the resultant array after q operations.


Approach:

Take a separate zero array s[] of same size as array A={1,2,3,4,5,..n} and perform all operations on that. 
Finally add that array to the array A

1. initialise s[] as zero array of size n
2. for every query increment l-1 index of array by val and decrement r index by val
3. then within the range each element of array can be added by its predecesor 
4. so from l-1 to r-1 every element is incremented by val
5. since r was earlier decremented the net increment wud remain zero and the succesive elements wudnt experience any increment
6. finally add the original array with each element of the sum array 
7. return the max value 

'''








def operations(arr, q):
    '''This function takes array arr as input and the list of queries q.
    Performs each query in list q on array arr and returns it'''
    s = [0 for i in range(len(arr))]#sum array to perform query operations
    #i is of form [l,r,val]
    for i in range(len(q)):
        s[q[i][0]-1] += q[i][-1]#increment l-1 index by val 
        if ((q[i][1]) < len(arr)):#to avoid IndexError
            s[q[i][1]] -= q[i][-1]#decrement r index element by val
    arr[0] += s[0]#element wise increment in original array arr[]
    for i in range(1, len(arr)):
        s[i] += s[i - 1]#incrementing every element in sum array by its predecessor
        arr[i] += s[i]# element wise addition
    return arr

if __name__=="__main__":
    lst=[i for i in range(1,int(input())+1)]#forming array {1,2,3,4,5,...n}
    Q=[]#list of queries 
    for i in range(int(input())):
        Q.append([int(x) for x in input().split()])
    print(max(operations(lst,Q)))#calling the operations function to return array after performing queries and returning its max value