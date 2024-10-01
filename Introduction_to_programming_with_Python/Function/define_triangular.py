def is_traigular(n):
    # return true is n is a triangular number
    # summation of n natural numbers = n(n+1)/2
    total = 0
    for i in range(n):
        total += i
        if total == n:
            print(True)
        print(False)

print(is_traigular(6))
