L1 = ['re']
L2 = ['mi']
L3 = ['do']

""""L4 = ['re','mi']"""
L4 = L1+L2
print(L4)

"""L3 = ['do'['re','mi']]"""
L3.append(L4)
print(L3)


"""L1 = ['re'['do'['re','mi']]]"""
L = L1.append(L3)
print(L)  
print(L1)  