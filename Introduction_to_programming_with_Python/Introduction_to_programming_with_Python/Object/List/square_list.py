def square_list(L):
    # square all the element of the of list value
    for i in range(len(L)):
        print(L)
        L[i] = L[i]**2
    return L

 

Lin = [2,3,2]
print(square_list(Lin))

bin = [2,3,5]
cin = Lin.extend(bin)
# print(cin)
