'''Pattern Question

Example : for  n =5
*****
** **
*   *
** **
*****

lets consider the string ***** the other strings can be obtained as a combination of the slices of the 
string and spaces

'''

def pattern(n):
    my_str=n*'*'
    print(my_str)
    
    #Now slicing string and adding spaces wherever required
    for i in range(n//2,0,-1):
        print(my_str[:i],my_str[n-i:],sep=(n-2*i)*' ')
    
    for i in range(2,n//2+1):
        print(my_str[:i],my_str[n-i:],sep=(n-2*i)*' ')
    
    
    print(my_str)
    return None

if __name__=="__main__":
    n=int(input())
    x=[]
    for i in range(n):
        x.append(int(input()))
    for _ in x:
        pattern(_)