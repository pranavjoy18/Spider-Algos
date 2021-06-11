'''Final Amount Problem

If workshop conducted and pizza given - Then increment of +x

If workshop conducted and pizza not given - Then decrement of y'''

class Algos:
    
    def __init__(self,a,b,c):
        '''a in input array containing n,r,x,y in order
        n- no of days 
        r- initial amount
        x- increment amount
        y- decrement amount
        
        b contains information about workshop , 1 if workshop conducted , 0 otherwise
        c contains information about pizza , 1 if pizza is given and 0 otherwise
        
        '''
        self.a=a
        self.b=b
        self.c=c
        self.s=0
   
    def finalamt(self):
        '''Returns the message based on the final amount , promoted if incremented ,demoted if decrement
        no change if unchanged'''
       
        for i in range(self.a[0]):
            
            #if workshop conducted on a day '1' and pizza given '1', then increment
            if self.b[i]=='1' and self.c[i]=='1':
                self.s+=self.a[2]
            
            # if workshop is conducted on day '1' and pizza not given '0' , then decrement
            elif self.b[i]=='1' and self.c[i]=='0':
                self.s-=self.a[3]
            
            #no change in other cases
            else:
                pass
        if self.s>0:
            print("promoted")
        elif self.s==0:
            print("no change")
        else:
            print("demoted")
            
if __name__=='__main__':
    a=[int(x) for x in input().split(' ')]
    b=[y for y in input().split(' ')]
    c=[z for z in input().split(' ')]
    algos=Algos(a,b,c)
    algos.finalamt()
    