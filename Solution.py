import time, math

"""
We will be checking only the numbers which don't contain the even digits. Because in cyclic rotation those digits 
will be at some point come at last and make the whole number even. For this we define and use the function evendigit

With this optimization our code will execute in less than 3 seconds
"""

a=time.time()
def evendigit(n):               #to rule out numbers containing any even digit  
    l = [int(d) for d in list(set(str(n)))]
    for d in l:
        if d%2==0:
            return False
    return True
def isprime(n):                 # checking if prime
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

n=2000000
c=1    # since 2 is also a prime we start our counting at 1 becuase the loop shall start form 3 
for i in range(3,n+1,2):
    if evendigit(i):
        
        s = str(i)
        l=[]
        for j in range(len(s)):
            s=s[1:]+s[0]
            l.append(int(s))   
        if all(list(map(isprime,l)))  :
            #print(i)
            c+=1
print(c)
print(time.time()-a)
#c=55 is the answer
