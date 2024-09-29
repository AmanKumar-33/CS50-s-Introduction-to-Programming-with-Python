#writing an code for finding the factorila of anumber using for lop

n = int(input("Enter the number: "))
fact = 1
for i in range(1,n+1):
    fact = fact *i
print("Factorial of",n,"is",fact)   