n=int(input("Enter a number "))
sqr=n**2
print("Square  of the number is ",sqr)
sqrrt=n**0.5
print("Square root of the number is ",sqrrt)
cube=n**3
print("Cube of the number is ",cube)
def check_prime(n):
    for i in range (2,n//2+1):
        if n%i==0:
            return False
    return True
result=check_prime(n)
print("Check for Prime ",result)
def factorial(a):
    fact=1
    for i in range (1,a+1):
        fact*=i
    return fact
result1=factorial(n)
print("Factorial is ",result1)
def primefactors(n):
    c=2
    while(n>1):
        if(n%c==0):
            print(c,end=" ")
            n=n/c
        else:
            c=c+1
primefactors(n)
