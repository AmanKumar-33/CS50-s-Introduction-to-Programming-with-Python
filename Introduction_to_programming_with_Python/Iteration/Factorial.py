#writing  code for finding the factorial of a number

x = int(input("Enter a number: "))
fact = 1
i =1
while i <= x:
    fact = fact *i
    i = i+1
print(f"{x}! factorial is {fact}")
