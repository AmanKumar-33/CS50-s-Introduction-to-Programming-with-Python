import math
def factorial(n):



  if not n>=0:
    raise ValueError("n must be greater than 0")
  if math.floor(n) !=n:
    raise ValueError("n must be exact integer")
  if n+1 == n:
    raise ValueError("value should be too large")
  result = 1
  factor = 2
  while factor <=n:
    result *= factor
    factor +=1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()