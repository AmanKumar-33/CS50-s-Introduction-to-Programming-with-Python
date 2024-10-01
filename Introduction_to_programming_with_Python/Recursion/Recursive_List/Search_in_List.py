#writing na program for searching na element in the list

def Search_in_list(L,e):
    if len(L) == 0:
        return False
    
    elif L[0] == e:
        return True
    else:
        return Search_in_list(L[1:],e)


test = [2,4,6,8] 
# e = 1
print(Search_in_list(test,1))