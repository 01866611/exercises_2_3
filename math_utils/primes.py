from math import sqrt
def isprime(n):
    if n==1:
        return False
    else:
        "check whether n is a prime number"
        for i in range(2,int(sqrt(n))+1):
            if (n%i==0):
                return False
        return True