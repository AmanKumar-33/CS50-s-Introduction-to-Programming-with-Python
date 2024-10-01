def remove_elem(L,e):
    """
    L is a list and e is the object 
    Retrun a new list with element in same order as L but 
    without element  any equal to e """
    newlist = []
    for i in L:
        # i is L[0],L[1],L[2]
        if i != e:
            newlist.append(i)
    return newlist

L = [1,2,2,2]
print(remove_elem(L,2))

L = [1,2,2,2]
print(remove_elem(L,1))

L = [1,2,2,2]
print(remove_elem(L,0))



