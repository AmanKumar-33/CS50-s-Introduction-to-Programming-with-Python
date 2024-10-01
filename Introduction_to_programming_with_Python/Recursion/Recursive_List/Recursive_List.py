#writing an program for the recursive List

def recursive_list(L):
    if (len(L) == 1):
        return L[0]
    else:
        return L[0] + recursive_list(L[1:])
    

test = [10,20,30,40,50,60]
    
print(recursive_list(test))
    
    