'''Symmetry 

Return the degrees of symmetry in a string

eg : abab has one degree of symmetry  ab-ab

eg:abababab has two degrees of symmetry
1. abab-abab
2.ab-ab

Assumption: only even length strings are given as inputs
'''

def symmetry(my_str):
    '''Function that returns the degrees of symmetry on an input string'''
    degree=0 # Initialise the degree of symmetry to zero
    
    #Split the string into 2 halves 
    left=my_str[:(len(my_str)+1)//2]
    right=my_str[(len(my_str)+1)//2:]
    
    #Compare the two halves for symmetry
    if left==right:
        degree+=1 # If the two halves are equal , then increment the degree of symmetry by 1
        degree+=symmetry(left) #Recursively find out if halves of the half string are symmetrical
    return degree

if __name__=='__main__':
    n=int(input())
    ip_str=input()
    assert len(ip_str)==n
    print(symmetry(ip_str))
