# Write a program that 
# :Ask the user for  a verb
# print I can _ better than you where you replace the _ with the verb the user entered
# then print the verb 5 times
s = "I can _ better than you"
verb = input("Enter a verb:")
print(s.replace("_",verb))
print((verb +' ')*5)

