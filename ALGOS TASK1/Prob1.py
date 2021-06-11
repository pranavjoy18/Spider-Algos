'''Binary String Problem

Given a binary string : Decompose it as an average of two other binary strings such that the 
difference between the decomposed strings is minimum

Print the two decomposed strings if their length is equal to the given input string 

Else print -1'''

if __name__=='__main__':
    n=int(input())
    ip_str=input()
    ''' For minimum difference between the decomposed strings , we take the immediate succesor and 
        the immediate predecessor ''' 
    a=bin(int(ip_str,2)-1)#decrementing the binary string by 1
    b=bin(int(ip_str,2)+1)#incrementing the binary string by 1
    
    l=len(ip_str)
    if len(a[2:])==len(b[2:]) and len(a[2:])==l:#Comparing if lengths of substrings are same as that of input string
    # A binary string has '0b' suffixed to it , so hence we slice the string from[2:] to obtain the string   
        print(a[2:],b[2:],sep=' ')
    else:
        print(-1)