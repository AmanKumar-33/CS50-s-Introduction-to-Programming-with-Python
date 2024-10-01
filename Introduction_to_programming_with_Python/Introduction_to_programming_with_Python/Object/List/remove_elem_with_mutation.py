def remove_elem(L,e):
    """Make a copy to save the element and then use L.clear() to empty 
    out the list and repopulate ones your keeping
    """

    #  copy the ement in new list
    newlist = L[:]
    # clear the original list 
    L.clear()
    for i in newlist:
        if e != i:
            L.append(i)

            




lin = [2,4,6,8,1,2,2]
remove_elem(lin,2)
print(lin)

L1 = [1,2,2,2]
remove_elem(L1,1)
print(L1)

L2 = [1,2,2,2]
# print(remove_elem(L,0))
remove_elem(L2,2)
print(L2)