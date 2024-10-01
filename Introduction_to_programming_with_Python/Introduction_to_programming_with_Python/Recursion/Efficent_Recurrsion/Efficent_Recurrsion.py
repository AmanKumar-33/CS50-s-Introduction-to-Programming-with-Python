# IN  this Script we will use dictionary to solve the problem  of the recurrsion where we
# intangle the function with the same function and we will use the dictionary to store the
# 
# 1. 0! = 1
# 2. n! = n*(n-1)! for n > 0 
# 3. n! = n*(n-1)*(n-2)! for n > 0
# 4. n! = n*(n-1)*(n-2)*(n-3)! for n > 0
# 5. n! = n*(n-1)*(n-2)*(n-3)*(n-4)! for n > 0
# 6. n! = n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)! for n > 0
# 7. n! = n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)! for n > 0

def factorial(n,d):
    if n in d:
        return d[n]
    else:
        ans = n * factorial(n-1,d)
        d[n] = ans
        return ans
    
d = {0:1,1:1}
print(factorial(6, d))
