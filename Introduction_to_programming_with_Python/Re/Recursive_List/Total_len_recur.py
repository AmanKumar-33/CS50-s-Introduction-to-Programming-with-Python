#writing na code for total length recursion

def total_len_recur(L):
    if len(L) == 1:
        return len(L[0])
    else:
        return len(L[0]) + total_len_recur(len(L[1:]))
    

test = ['ab',"c","df"]
print(total_len_recur(test))