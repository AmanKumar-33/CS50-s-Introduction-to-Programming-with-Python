#write a code for fibonacci series using recursion and memorization technique is used to reduce the time complexity

def fibonacci(n,d):
    if n in d:
        return d[n]
    else:
        ans = fibonacci(n-1,d) + fibonacci(n-2,d)
        d[n] = ans
        return ans
 
d = {0:0,1:1}
n = int(input("Enter the number of terms: "))
print(fibonacci(n,d))
