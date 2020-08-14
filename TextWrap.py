import textwrap

def wrap(string, max_width):
    k=0
    my=""
    i=0
    x=""
    while i!=len(string):
        k=0 
        my=""
        while k<max_width:
            my=my+string[i]
            k+=1 
            i+=1
            if(i==len(string)):
               break   
        #print(my)
        x=x+my+"\n"    
    return x   
        

    

if __name__ == '__main__':
    string=input()
    max_width=int(input())
    result = wrap(string, max_width)
    print(result)
