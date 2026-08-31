def magic(n):
    
    t=n
    while t>0:
        d=t%10
        s=s+d
        t=t//10
        
        return magic(t)
        
    
i=int(input("enter the number:"))
def is_magic(i):
    return magic(i) ==1







    
  
        
    
