'''Problem Statement:We are supposed find the longest proper prefix bracket sequence written by Inderraj

Approach:
Let us declare a variable _sum and another one maxi ,initialise both to zero

The main idea is to:
1.Increment the _sum by 1 when encountering opening bracket '<'
2.Decrement the _sum by 1 when encountering closing bracket'>'
3. Terminate when the _sum is 0 ,the length of the prefix bracket is 1+index of the string where _sum=0
4.Also in case if we encounter a closing bracket '>' right at the beginning of the string i.e _sum<0, 
we terminate, we need not have to update maxi as it is already initialised to zero
5. We then return maxi from the function
'''



def maxlen(string):
    '''This function takes a string and returns an integer which is the length of the longest prefix
    brackets in the given input string'''
    _sum = 0
    maxi = 0
    for i in range(len(string)):#Iterating through each element of the strinh
        if string[i] == '<':
            _sum += 1   
        else:
            _sum -= 1
        if _sum < 0:
            break
        if _sum == 0:
            maxi = i + 1
    return maxi

if __name__=="__main__":
    N=int(input())
    strings=[]#list of input strings
    for i in range(N):#inputs N strings 
        strings.append(input()) 
        
    for string in strings:
        print(maxlen(string))#prints the max length of prefix brackets in each string